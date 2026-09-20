from datetime import datetime

from memory import (
    update_user_profile,
    add_pending_task,
    add_completed_task,
    get_pending_tasks,
    get_completed_tasks
)


# =========================================================
# STUDY PLAN
# =========================================================

def create_study_plan(goal: str, days: int) -> dict:

    if days <= 0:

        return {
            "success": False,
            "message": "Study duration must be greater than 0 days."
        }

    goal_lower = goal.lower()

    if (
        "ai engineer" in goal_lower
        or "artificial intelligence" in goal_lower
        or goal_lower == "ai"
    ):

        topics = [
            "Python Programming",
            "Data Structures",
            "NumPy and Pandas",
            "Machine Learning",
            "Deep Learning",
            "Computer Vision",
            "Natural Language Processing",
            "Generative AI",
            "LLM Fundamentals",
            "Prompt Engineering",
            "Agentic AI",
            "AI Project Development",
            "Deployment",
            "Interview Preparation"
        ]

    elif "data analyst" in goal_lower:

        topics = [
            "Python",
            "NumPy",
            "Pandas",
            "Excel",
            "SQL",
            "Statistics",
            "Power BI",
            "Data Visualization",
            "Data Cleaning",
            "Data Analysis Project",
            "Interview Preparation"
        ]

    elif (
        "software engineer" in goal_lower
        or "software developer" in goal_lower
    ):

        topics = [
            "Python Programming",
            "Data Structures",
            "Algorithms",
            "OOP",
            "DBMS",
            "Operating Systems",
            "Computer Networks",
            "Git and GitHub",
            "Problem Solving",
            "Coding Practice",
            "Interview Preparation"
        ]

    else:

        topics = [
            "Programming Fundamentals",
            "Problem Solving",
            "Data Structures",
            "Algorithms",
            "Projects",
            "Communication Skills",
            "Interview Preparation"
        ]

    plan = []

    for day in range(1, days + 1):

        topic = topics[
            (day - 1) % len(topics)
        ]

        plan.append(
            {
                "day": day,
                "topic": topic,
                "task": (
                    f"Study {topic} and "
                    "complete one practical exercise."
                )
            }
        )

    return {
        "success": True,
        "goal": goal,
        "duration": days,
        "plan": plan
    }


# =========================================================
# PROGRESS
# =========================================================

def calculate_progress(
    completed: int,
    total: int
) -> dict:

    if total <= 0:

        return {
            "success": False,
            "message": "Total tasks must be greater than zero."
        }

    completed = max(
        0,
        min(completed, total)
    )

    percentage = round(
        (completed / total) * 100,
        2
    )

    return {
        "success": True,
        "completed": completed,
        "total": total,
        "percentage": percentage
    }


# =========================================================
# TASK MANAGEMENT
# =========================================================

def manage_task(
    action: str,
    task: str,
    completed_tasks: list
) -> dict:

    task = task.strip()

    if not task:

        return {
            "success": False,
            "message": "Task cannot be empty."
        }

    if action == "add":

        pending = get_pending_tasks()

        completed = get_completed_tasks()

        if task in pending:

            return {
                "success": False,
                "message": "Task is already pending."
            }

        if task in completed:

            return {
                "success": False,
                "message": "Task is already completed."
            }

        memory = add_pending_task(task)

        return {
            "success": True,
            "action": "add",
            "task": task,
            "pending_tasks": memory["pending_tasks"],
            "message": (
                f"Task '{task}' added successfully."
            )
        }

    elif action == "complete":

        completed = get_completed_tasks()

        if task in completed:

            return {
                "success": False,
                "message": "Task is already completed."
            }

        memory = add_completed_task(task)

        return {
            "success": True,
            "action": "complete",
            "task": task,
            "pending_tasks": memory["pending_tasks"],
            "completed_tasks": memory["completed_tasks"],
            "message": (
                f"Task '{task}' marked as completed."
            )
        }

    return {
        "success": False,
        "message": (
            "Invalid action. Use add or complete."
        )
    }


# =========================================================
# CAREER ADVICE
# =========================================================

def career_advice(
    career_goal: str,
    experience_level: str
) -> dict:

    goal = career_goal.lower()

    if "ai" in goal:

        roadmap = [
            "Python",
            "Data Structures",
            "Machine Learning",
            "Deep Learning",
            "Generative AI",
            "LLMs",
            "Agentic AI",
            "AI Projects",
            "Deployment",
            "Interview Preparation"
        ]

    elif "data analyst" in goal:

        roadmap = [
            "Excel",
            "SQL",
            "Statistics",
            "Python",
            "Pandas",
            "Power BI",
            "Data Visualization",
            "Projects",
            "Interview Preparation"
        ]

    elif "software" in goal:

        roadmap = [
            "Programming",
            "Data Structures",
            "Algorithms",
            "OOP",
            "DBMS",
            "Operating Systems",
            "Computer Networks",
            "Projects",
            "Coding Interviews"
        ]

    else:

        roadmap = [
            "Programming Fundamentals",
            "Problem Solving",
            "Technical Skills",
            "Projects",
            "Communication",
            "Interview Preparation"
        ]

    return {
        "success": True,
        "career_goal": career_goal,
        "experience_level": experience_level,
        "recommended_roadmap": roadmap,
        "advice": (
            "Build strong fundamentals, "
            "practice consistently, "
            "create real projects, and "
            "prepare for interviews."
        )
    }


# =========================================================
# PROFILE UPDATE
# =========================================================

def update_user_profile_tool(
    career_goal: str = "",
    experience_level: str = "",
    study_days: int = 0
) -> dict:

    memory = update_user_profile(
        career_goal=(
            career_goal
            if career_goal
            else None
        ),
        experience_level=(
            experience_level
            if experience_level
            else None
        ),
        study_days=(
            study_days
            if study_days > 0
            else None
        )
    )

    return {
        "success": True,
        "career_goal": memory["career_goal"],
        "experience_level": memory["experience_level"],
        "study_days": memory["study_days"],
        "message": "User profile updated successfully."
    }


# =========================================================
# DATE
# =========================================================

def get_current_date():

    return {
        "success": True,
        "date": datetime.now().strftime(
            "%Y-%m-%d"
        )
    }


# =========================================================
# TOOL EXECUTOR
# =========================================================

def execute_tool(
    tool_name: str,
    arguments: dict,
    completed_tasks: list
):

    if tool_name == "update_user_profile_tool":

        return update_user_profile_tool(
            arguments.get("career_goal", ""),
            arguments.get("experience_level", ""),
            arguments.get("study_days", 0)
        )

    elif tool_name == "create_study_plan":

        return create_study_plan(
            arguments.get("goal", ""),
            arguments.get("days", 30)
        )

    elif tool_name == "calculate_progress":

        return calculate_progress(
            arguments.get("completed", 0),
            arguments.get("total", 0)
        )

    elif tool_name == "manage_task":

        return manage_task(
            arguments.get("action", ""),
            arguments.get("task", ""),
            completed_tasks
        )

    elif tool_name == "career_advice":

        return career_advice(
            arguments.get("career_goal", ""),
            arguments.get(
                "experience_level",
                "beginner"
            )
        )

    elif tool_name == "get_current_date":

        return get_current_date()

    return {
        "success": False,
        "message": f"Unknown tool: {tool_name}"
    }