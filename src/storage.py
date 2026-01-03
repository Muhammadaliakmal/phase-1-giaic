from typing import List, Dict, Optional
from .models import Task

# In-memory storage for tasks
_tasks: Dict[int, Task] = {}
_next_id: int = 1

def add_task(title: str, description: str) -> Task:
    """
    Adds a new task to the in-memory storage.
    """
    global _next_id
    new_task = Task(id=_next_id, title=title, description=description)
    _tasks[_next_id] = new_task
    _next_id += 1
    return new_task

def get_all_tasks() -> List[Task]:
    """
    Returns a list of all tasks.
    """
    return list(_tasks.values())

def get_task_by_id(task_id: int) -> Optional[Task]:
    """
    Retrieves a task by its ID.
    """
    return _tasks.get(task_id)

def update_task(task_id: int, title: str, description: str, completed: bool) -> Optional[Task]:
    """
    Updates an existing task.
    """
    if task_id in _tasks:
        task = _tasks[task_id]
        task.title = title
        task.description = description
        task.completed = completed
        return task
    return None

def delete_task(task_id: int) -> bool:
    """
    Deletes a task by its ID. Returns True if successful, False otherwise.
    """
    if task_id in _tasks:
        del _tasks[task_id]
        return True
    return False
