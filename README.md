# Employee Management System

This is a simple command-line interface (CLI) based Employee Management System. It allows you to manage employees, departments, projects, and leaves using SQLite as the database. The project demonstrates basic CRUD (Create, Read, Update, Delete) operations.

## Table of Contents

- [Features](#features)
- [Directory Structure](#directory-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Acknowledgements](#acknowledgements)

## Features

- Add, view, update, and delete employees.
- Add, view, update, and delete departments.
- Add, view, update, and delete projects.
- Add, view, update, and delete leaves for employees.
- View employees by department.
- View specific employee details by ID.
- View leaves for a specific employee.

## Directory Structure
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
├── models
│ ├── init.py
│ ├── init_db.py
│ ├── employee.py
│ ├── department.py
│ ├── project.py
│ └── leave.py
├── cli.py
├── debug.py
└── helpers.py

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
Install dependencies:

Ensure you have pipenv installed. Then run:

bash
Copy code
pipenv install
pipenv shell
Initialize the database:

Run the database initialization script:

bash
Copy code
python -m lib.models.init_db
Usage
Run the CLI:

bash
Copy code
python lib/cli.py
Follow the on-screen instructions to manage employees, departments, projects, and leaves.

CLI Menu Options
Add a new employee
View all employees
View employees by department
Delete an employee
Add a new department
View all departments
Delete a department
Add a new project
View all projects
Delete a project
Add a leave for an employee
View leaves for an employee
Update an employee
Update a department
Update a project
Update a leave
View an employee by ID
Delete a leave
Exit the program
Database Schema
Employees
Column	Type
id	INTEGER
name	TEXT
age	INTEGER
department_id	INTEGER
Departments
Column	Type
id	INTEGER
name	TEXT
Projects
Column	Type
id	INTEGER
name	TEXT
description	TEXT
Leaves
Column	Type
id	INTEGER
employee_id	INTEGER
start_date	TEXT
end_date	TEXT
reason	TEXT

Acknowledgements
This project is based on the template and curriculum provided by Flatiron School. It uses SQLite for data storage and tabulate for formatting output in the CLI.
