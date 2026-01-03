""" prompt
/sp.constitution

Project: Phase-1 In-Memory Todo Console Application

Core Principles:
- Spec-driven development is mandatory
- No implementation without an approved specification
- In-memory storage only (no files, no database)
- Simple, readable, maintainable Python code

Domain Rules:
- A Task has: id, title, description, completed
- id is unique and auto-incremented
- title must not be empty
- completed defaults to false

Technical Constraints:
- Python 3.13+
- Console application only
- No external frameworks

Quality Standards:
- Single Responsibility Principle
- Explicit error handling
- Clear user feedback for every action


/sp.specification

Name: Todo Core (Phase-1)
Level: Basic
Type: In-Memory Console Application

Objective:
Build a command-line todo application that stores tasks in memory.

Features:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete / Incomplete

Task Model:
- id: integer
- title: string
- description: string
- completed: boolean

Behavior Rules:
- Tasks exist only during program execution
- Tasks are stored in memory
- Tasks are referenced by ID

Constraints:
- Empty title is invalid
- Operations on invalid IDs must return errors

Out of Scope:
- Persistence
- Authentication
- GUI or Web interface


/sp.plan

Input:
- constitution.md
- specs/todo.spec.md

Goal:
Plan the implementation of the Phase-1 Todo application.

Produce:
- High-level architecture
- Module responsibilities
- Execution flow of the application

Constraints:
- Clean separation of concerns
- In-memory data handling
- Console-based interaction

No code generation.


/sp.tasks

Input:
- specs/todo.spec.md
- Implementation plan

Break down the project into concrete development tasks.

Each task should include:
- Task name
- Description
- Related feature
- Expected output file

Scope:
- Domain model
- In-memory storage
- Business logic
- CLI interaction


/sp.implement

Input:
- constitution.md
- specs/todo.spec.md
- Planned tasks

Implement the Phase-1 Todo application.

Requirements:
- Python 3.13+
- In-memory storage
- Console-based menu
- Implement all 5 basic features

Output files:
- src/models.py
- src/storage.py
- src/services.py
- src/main.py

Follow clean code principles.
"""
