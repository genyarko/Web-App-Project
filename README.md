# Task Manager Web Application

This is a simple web application for managing tasks. Users can register, log in, create, view, update, and delete tasks. The application is built with Flask, SQLAlchemy, and Flask-Login, and uses SQLite for local development.

## Features

- User Authentication:
  - Register with an email and password
  - Log in and log out
- Task Management:
  - Create a new task with a title and description
  - View a list of all tasks
  - Update task titles and descriptions
  - Delete tasks
- Database:
  - Uses SQLite for local development
  - Supports user-specific task management

## Prerequisites

- Python 3.x
- Flask
- SQLAlchemy
- Flask-Login
- pyodbc (if using SQL Server)
- SQLite (for local development)

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/genyarko/Web-App-Project.git
cd Web-App-Project

**Application Structure**
task_manager/
├── app.py
├── config.py
├── models.py
├── routes/
│   ├── __init__.py
│   ├── auth.py
│   └── tasks.py
├── templates/
│   ├── layout.html
│   ├── login.html
│   ├── register.html
│   ├── tasks.html
│   ├── new_task.html
│   └── edit_task.html
├── static/
│   └── css/
│       └── styles.css
└── requirements.txt

