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