# Employee Management System

This is a simple command-line interface (CLI) based Employee Management System. It allows you to manage employees, departments, projects, and leaves using SQLite as the database. The project demonstrates basic CRUD (Create, Read, Update, Delete) operations.

## Table of Contents

- [Features](#features)
- [Directory Structure](#directory-structure)
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
   git clone https://github.com/Alvooh/python-phase3-final-project-EMS

   cd python-phase3-final-project-EMS

Install dependencies:

Ensure you have pipenv installed. Then run:

```bash

pipenv install
pipenv shell
```
# Initialize the database:
Run the database initialization script:

```bash
python -m lib.models.init_db.py

```
Run the CLI:

```bash
python lib/cli.py
```
Follow the on-screen instructions to manage employees, departments, projects, and leaves.

# CLI Menu Options
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


# Acknowledgements

This project is based on the template and curriculum provided by Flatiron School. It uses SQLite for data storage and tabulate for formatting output in the CLI.

### Author

This project has been authored by Alvin Obala [[github.com/Alvooh]]

### License

Copyright (c) 2024 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


