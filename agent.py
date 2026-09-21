import json

import streamlit as st

from google import genai
from google.genai import types

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)

from memory import (
    load_memory,
    add_conversation,
    get_completed_tasks
)

from tools import execute_tool

client = genai.Client(
    api_key=GEMINI_API_KEY
)


SYSTEM_INSTRUCTIONS = """
You are an intelligent Agentic AI Career Assistant.

You help users with:

- Career planning
- AI Engineer preparation
- Programming
- Learning plans
- Interview preparation
- Study progress
- Career advice
- Tasks
- General questions

IMPORTANT:

Answer normal questions directly.

Use tools when useful.

CAREER GOAL DETECTION:

Understand the user's meaning semantically.

Do NOT require an exact sentence.

Examples:

"My career goal is AI engineer"

"I want to become an AI engineer"

"I am planning to become an artificial intelligence engineer"

"I want to build my career in AI"

"I am preparing for an AI Engineer career"

All of these mean the user wants an AI Engineer career goal.

When a career goal is detected,
call update_user_profile_tool.

If the user asks for a study plan,
use create_study_plan.

If the user asks to add or complete a task,
use manage_task.

If the user asks about progress,
use calculate_progress.

If the user asks for a career roadmap,
use career_advice.

If the user asks the current date,
use get_current_date.

Do not use tools unnecessarily.

Always provide a natural helpful final response.
"""


UPDATE_PROFILE = types.FunctionDeclaration(
    name="update_user_profile_tool",
    description=(
        "Save or update the user's career profile. "
        "Use this whenever the user communicates "
        "a career goal or profile information."
    ),
    parameters=types.Schema(
        type="OBJECT",
        properties={
            "career_goal": types.Schema(
                type="STRING"
            ),
            "experience_level": types.Schema(
                type="STRING"
            ),
            "study_days": types.Schema(
                type="INTEGER"
            )
        }
    )
)


STUDY_PLAN = types.FunctionDeclaration(
    name="create_study_plan",
    description=(
        "Create a personalized study plan "
        "for a career goal."
    ),
    parameters=types.Schema(
        type="OBJECT",
        properties={
            "goal": types.Schema(
                type="STRING"
            ),
            "days": types.Schema(
                type="INTEGER"
            )
        },
        required=[
            "goal",
            "days"
        ]
    )
)


PROGRESS = types.FunctionDeclaration(
    name="calculate_progress",
    description=(
        "Calculate learning progress."
    ),
    parameters=types.Schema(
        type="OBJECT",
        properties={
            "completed": types.Schema(
                type="INTEGER"
            ),
            "total": types.Schema(
                type="INTEGER"
            )
        },
        required=[
            "completed",
            "total"
        ]
    )
)


TASK = types.FunctionDeclaration(
    name="manage_task",
    description=(
        "Add or complete a learning task."
    ),
    parameters=types.Schema(
        type="OBJECT",
        properties={
            "action": types.Schema(
                type="STRING",
                enum=[
                    "add",
                    "complete"
                ]
            ),
            "task": types.Schema(
                type="STRING"
            )
        },
        required=[
            "action",
            "task"
        ]
    )
)


CAREER_ADVICE = types.FunctionDeclaration(
    name="career_advice",
    description=(
        "Give a career roadmap and advice."
    ),
    parameters=types.Schema(
        type="OBJECT",
        properties={
            "career_goal": types.Schema(
                type="STRING"
            ),
            "experience_level": types.Schema(
                type="STRING"
            )
        },
        required=[
            "career_goal",
            "experience_level"
        ]
    )
)


DATE_TOOL = types.FunctionDeclaration(
    name="get_current_date",
    description="Get today's date.",
    parameters=types.Schema(
        type="OBJECT",
        properties={}
    )
)


GEMINI_TOOLS = [
    types.Tool(
        function_declarations=[
            UPDATE_PROFILE,
            STUDY_PLAN,
            PROGRESS,
            TASK,
            CAREER_ADVICE,
            DATE_TOOL
        ]
    )
]


def generate_response(contents):

    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTIONS,
        tools=GEMINI_TOOLS
    )

    return client.models.generate_content(
        model=GEMINI_MODEL,
        contents=contents,
        config=config
    )


    if not result.get("success"):

        return result.get(
            "message",
            "Unable to create study plan."
        )

    lines = []

    lines.append(
        f"## 📚 {result['duration']}-Day "
        f"{result['goal']} Study Plan"
    )

    lines.append("")

    for item in result["plan"]:

        lines.append(
            f"### Day {item['day']} — "
            f"{item['topic']}"
        )

        lines.append(
            f"- {item['task']}"
        )

        lines.append("")

    return "\n".join(lines)

def run_agent(user_input):

    memory = load_memory()

    career_goal = memory.get(
        "career_goal",
        ""
    )

    experience_level = memory.get(
        "experience_level",
        "beginner"
    )

    study_days = memory.get(
        "study_days",
        30
    )

    completed_tasks = get_completed_tasks()

    user_context = f"""
USER PROFILE

Career Goal:
{career_goal if career_goal else "Not set"}

Experience Level:
{experience_level}

Study Days:
{study_days}

Completed Tasks:
{completed_tasks}

USER MESSAGE:
{user_input}
"""

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part(
                    text=user_context
                )
            ]
        )
    ]

    for _ in range(5):

        try:

            response = generate_response(
                contents
            )

        except Exception as e:

            return (
                "❌ Gemini API Error\n\n"
                f"```text\n{str(e)}\n```"
            )

        if response.text:

            answer = response.text.strip()

            add_conversation(
                user_input,
                answer
            )

            return answer


        function_calls = []

        if response.candidates:

            content = (
                response.candidates[0].content
            )

            if content:

                for part in content.parts:

                    if part.function_call:

                        function_calls.append(
                            part.function_call
                        )

        if not function_calls:

            return (
                "I couldn't generate a response. "
                "Please try again."
            )

        tool_results = []

        for function_call in function_calls:

            tool_name = function_call.name

            arguments = dict(
                function_call.args
            )

            st.info(
                f"🔧 Agent selected tool: "
                f"`{tool_name}`"
            )

            if arguments:

                with st.expander(
                    "🔍 View tool arguments"
                ):

                    st.json(arguments)

         
            result = execute_tool(
                tool_name,
                arguments,
                completed_tasks
            )

            if result.get("success"):

                st.success(
                    "✅ Tool executed successfully"
                )

            else:

                st.warning(
                    "⚠️ Tool returned an issue"
                )

            
            if (
                tool_name == "create_study_plan"
                and result.get("success")
            ):

                answer = format_study_plan(
                    result
                )

                add_conversation(
                    user_input,
                    answer
                )

                return answer


            if (
                tool_name
                == "update_user_profile_tool"
                and result.get("success")
            ):

                goal = result.get(
                    "career_goal",
                    ""
                )

                if goal:

                    answer = (
                        "✅ Got it! I've saved your "
                        f"career goal as **{goal}**."
                    )

                    add_conversation(
                        user_input,
                        answer
                    )

                    return answer

            tool_results.append(
                {
                    "tool": tool_name,
                    "result": result
                }
            )

       
        contents.append(
            response.candidates[0].content
        )

        contents.append(
            types.Content(
                role="user",
                parts=[
                    types.Part(
                        text=(
                            "Tool execution results:\n"
                            + json.dumps(
                                tool_results,
                                ensure_ascii=False,
                                default=str
                            )
                            + "\n\n"
                            "Now provide the final answer "
                            "to the user."
                        )
                    )
                ]
            )
        )

    return (
        "⚠️ The agent reached its maximum "
        "number of steps. Please try again."
    )
