# task-management-api

A RESTful API for managing tasks, built with Django and Django REST Framework (DRF). This project allows users to manage their tasks by creating, updating, deleting, and marking tasks as complete or incomplete.

## Features

- **User Authentication**:
  - Register, login, and logout functionality.
  - Token-based authentication (JWT).
  
- **Task Management (CRUD)**:
  - Create, Read, Update, and Delete tasks.
  - Fields: Title, Description, Due Date, Priority (Low, Medium, High), and Status (Pending, Completed).

- **Task Ownership**:
  - Each user can manage only their own tasks.
  - Permissions prevent unauthorized access to tasks.

- **Mark Tasks Complete/Incomplete**:
  - Timestamp when a task is marked as complete.
  - Restrict editing of completed tasks unless reverted to incomplete.

- **Task Filters and Sorting**:
  - Filter by Status (Pending/Completed), Priority, and Due Date.
  - Sort tasks by Due Date or Priority.

- **Deployment**:
  - Fully deployed on [Heroku/PythonAnywhere].

## Getting Started

### Prerequisites

- Python 3.8+
- Django 4.0+
- Django REST Framework

