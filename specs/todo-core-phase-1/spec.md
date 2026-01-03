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
