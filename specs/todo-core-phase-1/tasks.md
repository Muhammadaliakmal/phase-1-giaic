# Development Tasks: Todo Core (Phase-1)

This document breaks down the implementation into concrete, actionable tasks based on the project specification and architectural plan.

---

### Task 1: Define Domain Model

-   **Task Name:** Create Task Model
-   **Description:** Define the data structure for a Task. It should be a class or dataclass containing `id`, `title`, `description`, and `completed` fields with their respective types.
-   **Related Feature:** Task Model
-   **Expected Output File:** `src/models.py`

---

### Task 2: Implement In-Memory Storage

-   **Task Name:** Create Task Storage Manager
-   **Description:** Implement the logic for storing tasks in an in-memory list. This module will handle creating, retrieving, updating, and deleting tasks from the list. It will also manage the auto-incrementing of task IDs.
-   **Related Feature:** All (Core Storage)
-   **Expected Output File:** `src/storage.py`

---

### Task 3: Implement Business Logic Services

-   **Task Name:** Create Task Services
-   **Description:** Implement the business logic for each feature. This service layer will interact with the storage module and enforce rules, such as preventing tasks with empty titles. It will contain functions for all primary user actions.
-   **Related Feature:** Add Task, View Tasks, Update Task, Delete Task, Mark Task Complete
-   **Expected Output File:** `src/services.py`

---

### Task 4: Implement CLI User Interface

-   **Task Name:** Build Console UI and Application Loop
-   **Description:** Create the main entry point of the application. This file will be responsible for the user-facing menu, handling user input, and calling the appropriate service functions. It will manage the main application loop and display feedback to the user.
-   **Related Feature:** All (CLI)
-   **Expected Output File:** `src/main.py`
