# Implementation Plan: Todo Core (Phase-1)

## 1. High-Level Architecture

The application will follow a simple, layered architecture to ensure a clean separation of concerns as mandated by the constitution.

-   **Presentation Layer (`main.py`):** Handles all user interaction (displaying menus, getting user input) and orchestrates the application flow. It will not contain any business logic.
-   **Service Layer (`services.py`):** Contains the core business logic for managing tasks (adding, updating, deleting, etc.). It acts as an intermediary between the presentation layer and the data layer.
-   **Data Layer (`storage.py`):** Responsible for the in-memory storage of tasks. It will provide a simple API for CRUD (Create, Read, Update, Delete) operations on the task list.
-   **Domain Model (`models.py`):** Defines the `Task` data structure as specified in the domain rules.

## 2. Module Responsibilities

-   **`src/models.py`:**
    -   Will contain the `Task` class (or a dataclass/TypedDict) with attributes: `id` (int), `title` (str), `description` (str), and `completed` (bool).

-   **`src/storage.py`:**
    -   Will manage a private list of `Task` objects in memory.
    -   Will handle the auto-incrementing `id` for new tasks.
    -   Will expose functions like `add_task`, `get_task_by_id`, `get_all_tasks`, `update_task`, and `delete_task`.

-   **`src/services.py`:**
    -   Will import functions from `storage.py` to manipulate data.
    -   Will contain functions that map to user features, like `create_new_task`, `view_all_tasks`, `update_existing_task`, etc.
    -   Will enforce business rules, such as validating that a title is not empty before creating a task, or handling errors for invalid IDs.

-   **`src/main.py`:**
    -   Will contain the main application loop (`while True`).
    -   Will display a menu of options to the user (Add, View, Update, etc.).
    -   Will capture user input.
    -   Will call the appropriate functions from the `services.py` module based on user choice.
    -   Will be responsible for printing task data and feedback messages to the console.

## 3. Execution Flow

1.  The user starts the application by running `python src/main.py`.
2.  `main.py` enters a loop and displays the main menu.
3.  The user selects an option (e.g., '1' to add a task).
4.  `main.py` prompts for necessary input (e.g., title and description).
5.  `main.py` calls the corresponding function in `services.py` (e.g., `services.create_new_task(title, description)`).
6.  The service function in `services.py` validates the input (e.g., checks for an empty title).
7.  If valid, the service function calls the appropriate data function in `storage.py` (e.g., `storage.add_task(title, description)`).
8.  `storage.py` creates a new `Task` object, assigns it a new ID, and adds it to the in-memory list.
9.  Control returns up the call stack.
10. `main.py` displays a success or error message to the user.
11. The loop continues, and the menu is displayed again.

This plan adheres to the in-memory storage constraint and separates the console interaction from the business logic.
