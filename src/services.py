from typing import List, Optional
from . import storage
from .models import Task

def create_task(title: str, description: str) -> (Optional[Task], Optional[str]):
    """
    Creates a new task. Enforces business rules.
    """
    if not title:
        return None, "Title cannot be empty."
    
    task = storage.add_task(title, description)
    return task, None

def find_all_tasks() -> List[Task]:
    """
    Retrieves all tasks.
    """
    return storage.get_all_tasks()

def find_task_by_id(task_id: int) -> Optional[Task]:
    """
    Finds a task by its ID.
    """
    return storage.get_task_by_id(task_id)

def edit_task(task_id: int, title: str, description: str) -> (Optional[Task], Optional[str]):
    """
    Updates a task's title and description.
    """
    if not title:
        return None, "Title cannot be empty."
        
    task = find_task_by_id(task_id)
    if not task:
        return None, "Task not found."
        
    updated_task = storage.update_task(task_id, title, description, task.completed)
    return updated_task, None

def toggle_task_completion(task_id: int) -> (Optional[Task], Optional[str]):
    """
    Marks a task as complete or incomplete.
    """
    task = find_task_by_id(task_id)
    if not task:
        return None, "Task not found."
        
    updated_task = storage.update_task(task_id, task.title, task.description, not task.completed)
    return updated_task, None

def remove_task(task_id: int) -> (bool, Optional[str]):
    """
    Deletes a task.
    """
    if not find_task_by_id(task_id):
        return False, "Task not found."
    
    success = storage.delete_task(task_id)
    return success, None

