import streamlit as st

from agent import run_agent

from memory import (
    load_memory,
    clear_memory,
    update_career_goal
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Agentic AI Career Assistant",
    page_icon="🤖",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title(
    "🤖 Agentic AI Career Assistant"
)

st.caption(
    "AI-powered career planning, learning, "
    "task management and progress tracking"
)


# =========================================================
# LOAD MEMORY
# =========================================================

memory = load_memory()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("👤 User Profile")

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

    pending_tasks = memory.get(
        "pending_tasks",
        []
    )

    completed_tasks = memory.get(
        "completed_tasks",
        []
    )

    # -----------------------------------------------------
    # PROFILE
    # -----------------------------------------------------

    st.subheader(
        "🎯 Career Profile"
    )

    new_career_goal = st.text_input(
        "Career Goal",
        value=career_goal,
        placeholder="Example: AI Engineer"
    )

    experience_options = [
        "beginner",
        "intermediate",
        "advanced"
    ]

    if experience_level not in experience_options:

        experience_level = "beginner"

    new_experience_level = st.selectbox(
        "Experience Level",
        experience_options,
        index=experience_options.index(
            experience_level
        )
    )

    new_study_days = st.number_input(
        "Study Days",
        min_value=1,
        max_value=365,
        value=int(study_days),
        step=1
    )

    if st.button(
        "💾 Save Profile",
        use_container_width=True
    ):

        update_career_goal(
            new_career_goal,
            new_experience_level,
            new_study_days
        )

        st.success(
            "✅ Profile saved!"
        )

        st.rerun()

    st.divider()

    # -----------------------------------------------------
    # PROFILE SUMMARY
    # -----------------------------------------------------

    st.write(
        f"**🎯 Career:** "
        f"{career_goal if career_goal else 'Not set'}"
    )

    st.write(
        f"**📈 Level:** {experience_level}"
    )

    st.write(
        f"**📅 Study Days:** {study_days}"
    )

    st.divider()

    # -----------------------------------------------------
    # PENDING TASKS
    # -----------------------------------------------------

    st.subheader(
        "📋 Pending Tasks"
    )

    if pending_tasks:

        for index, task in enumerate(
            pending_tasks,
            start=1
        ):

            st.write(
                f"⏳ {index}. {task}"
            )

    else:

        st.caption(
            "No pending tasks."
        )

    st.divider()

    # -----------------------------------------------------
    # COMPLETED TASKS
    # -----------------------------------------------------

    st.subheader(
        "✅ Completed Tasks"
    )

    completed_count = len(
        completed_tasks
    )

    st.metric(
        "Completed",
        completed_count
    )

    if completed_tasks:

        for index, task in enumerate(
            completed_tasks,
            start=1
        ):

            st.write(
                f"✅ {index}. {task}"
            )

    else:

        st.caption(
            "No completed tasks yet."
        )

    st.divider()

    # -----------------------------------------------------
    # CLEAR MEMORY
    # -----------------------------------------------------

    if st.button(
        "🗑️ Clear Memory",
        use_container_width=True
    ):

        clear_memory()

        st.session_state.messages = []

        st.success(
            "Memory cleared!"
        )

        st.rerun()


# =========================================================
# CHAT HISTORY
# =========================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# =========================================================
# CHAT INPUT
# =========================================================

user_input = st.chat_input(
    "Ask your career assistant..."
)


# =========================================================
# PROCESS USER MESSAGE
# =========================================================

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):

        st.markdown(
            user_input
        )

    with st.chat_message("assistant"):

        with st.spinner(
            "🤖 Agent is thinking..."
        ):

            try:

                answer = run_agent(
                    user_input
                )

                st.markdown(
                    answer
                )

            except Exception as e:

                answer = (
                    "❌ An unexpected error occurred.\n\n"
                    f"```text\n{str(e)}\n```"
                )

                st.error(
                    answer
                )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )