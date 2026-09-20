import json
import os


MEMORY_FILE = "user_memory.json"


def default_memory():
    return {
        "career_goal": "",
        "experience_level": "beginner",
        "study_days": 30,
        "pending_tasks": [],
        "completed_tasks": [],
        "conversation_history": []
    }


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return default_memory()

    try:

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            memory = json.load(file)

        default = default_memory()

        for key, value in default.items():

            if key not in memory:
                memory[key] = value

        return memory

    except (
        json.JSONDecodeError,
        OSError
    ):

        return default_memory()


def save_memory(memory):

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            memory,
            file,
            indent=4,
            ensure_ascii=False
        )


def update_career_goal(
    career_goal,
    experience_level="beginner",
    study_days=30
):

    memory = load_memory()

    memory["career_goal"] = career_goal
    memory["experience_level"] = experience_level
    memory["study_days"] = study_days

    save_memory(memory)

    return memory


def update_user_profile(
    career_goal=None,
    experience_level=None,
    study_days=None
):

    memory = load_memory()

    if career_goal:
        memory["career_goal"] = career_goal

    if experience_level:
        memory["experience_level"] = experience_level

    if study_days is not None:
        memory["study_days"] = study_days

    save_memory(memory)

    return memory


def add_pending_task(task):

    memory = load_memory()

    task = task.strip()

    if task and task not in memory["pending_tasks"]:

        memory["pending_tasks"].append(task)

    save_memory(memory)

    return memory


def get_pending_tasks():

    memory = load_memory()

    return memory.get(
        "pending_tasks",
        []
    )


def add_completed_task(task):

    memory = load_memory()

    task = task.strip()

    if not task:
        return memory

    if task in memory["pending_tasks"]:

        memory["pending_tasks"].remove(task)

    if task not in memory["completed_tasks"]:

        memory["completed_tasks"].append(task)

    save_memory(memory)

    return memory


def get_completed_tasks():

    memory = load_memory()

    return memory.get(
        "completed_tasks",
        []
    )


def add_conversation(
    user_message,
    assistant_message
):

    memory = load_memory()

    memory["conversation_history"].append(
        {
            "user": user_message,
            "assistant": assistant_message
        }
    )

    memory["conversation_history"] = (
        memory["conversation_history"][-20:]
    )

    save_memory(memory)

    return memory


def get_conversation_history():

    memory = load_memory()

    return memory.get(
        "conversation_history",
        []
    )


def clear_memory():

    memory = default_memory()

    save_memory(memory)

    return memory