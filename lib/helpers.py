from tabulate import tabulate
from models import get_connection
from models.employee import create_employee, get_all_employees, get_employees_by_department, delete_employee, update_employee, get_employee_by_id
from models.department import create_department, get_all_departments, delete_department, update_department
from models.project import create_project, get_all_projects, delete_project, update_project
from models.leave import create_leave, get_leaves_by_employee, update_leave

def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department_id = int(input("Enter employee department ID: "))
    salary = int(input("Enter employee salary: "))

    conn = get_connection()
    create_employee(conn, name, age, department_id, salary)
    conn.close()
    print(f"Employee {name} added.")

def view_employees():
    conn = get_connection()
    employees = get_all_employees(conn)
    conn.close()
    table = [[emp[0], emp[1], emp[2], emp[3], emp[4]] for emp in employees]
    print(tabulate(table, headers=["ID", "Name", "Age", "Department ID", "Salary"]))

def view_employees_by_department():
    department_id = int(input("Enter department ID to filter employees: "))
    conn = get_connection()
    employees = get_employees_by_department(conn, department_id)
    conn.close()
    if employees:
        table = [[emp[0], emp[1], emp[2], emp[3], emp[4]] for emp in employees]
        print(tabulate(table, headers=["ID", "Name", "Age", "Department ID", "Salary"]))
    else:
        print(f"No employees found in department ID {department_id}")

def delete_employee_helper():
    emp_id = int(input("Enter employee ID to delete: "))
    conn = get_connection()
    delete_employee(conn, emp_id)
    conn.close()
    print(f"Employee with ID {emp_id} deleted.")

def add_department():
    name = input("Enter department name: ")
    description = input("Enter department description: ")

    conn = get_connection()
    create_department(conn, name, description)
    conn.close()
    print(f"Department {name} added.")

def view_departments():
    conn = get_connection()
    departments = get_all_departments(conn)
    conn.close()
    table = [[dept[0], dept[1], dept[2]] for dept in departments]
    print(tabulate(table, headers=["ID", "Name", "Description"]))

def delete_department_helper():
    dept_id = int(input("Enter department ID to delete: "))
    conn = get_connection()
    delete_department(conn, dept_id)
    conn.close()
    print(f"Department with ID {dept_id} deleted.")

def add_project():
    name = input("Enter project name: ")
    description = input("Enter project description: ")
    department_id = int(input("Enter department ID: "))

    conn = get_connection()
    create_project(conn, name, description, department_id)
    conn.close()
    print(f"Project {name} added.")

def view_projects():
    conn = get_connection()
    projects = get_all_projects(conn)
    conn.close()
    table = [[proj[0], proj[1], proj[2], proj[3]] for proj in projects]
    print(tabulate(table, headers=["ID", "Name", "Description", "Department ID"]))

def delete_project_helper():
    project_id = int(input("Enter project ID to delete: "))
    conn = get_connection()
    delete_project(conn, project_id)
    conn.close()
    print(f"Project with ID {project_id} deleted.")

def add_leave():
    employee_id = int(input("Enter employee ID: "))
    start_date = input("Enter leave start date (YYYY-MM-DD): ")
    end_date = input("Enter leave end date (YYYY-MM-DD): ")
    reason = input("Enter leave reason: ")

    conn = get_connection()
    create_leave(conn, employee_id, start_date, end_date, reason)
    conn.close()
    print(f"Leave for employee ID {employee_id} added.")

def view_employee_leaves():
    employee_id = int(input("Enter employee ID to view leaves: "))
    conn = get_connection()
    leaves = get_leaves_by_employee(conn, employee_id)
    conn.close()
    if leaves:
        table = [[leave[0], leave[1], leave[2], leave[3], leave[4]] for leave in leaves]
        print(tabulate(table, headers=["ID", "Employee ID", "Start Date", "End Date", "Reason"]))
    else:
        print(f"No leaves found for employee ID {employee_id}")

def view_employee_by_id():
    emp_id = int(input("Enter employee ID to view: "))
    conn = get_connection()
    employee = get_employee_by_id(conn, emp_id)
    conn.close()
    if employee:
        table = [[employee[0], employee[1], employee[2], employee[3], employee[4]]]
        print(tabulate(table, headers=["ID", "Name", "Age", "Department ID", "Salary"]))
    else:
        print(f"No employee found with ID {emp_id}")

def view_employee_leaves():
    employee_id = int(input("Enter employee ID to view leaves: "))
    conn = get_connection()
    leaves = get_leaves_by_employee(conn, employee_id)
    conn.close()
    if leaves:
        table = [[leave[0], leave[1], leave[2], leave[3], leave[4]] for leave in leaves]
        print(tabulate(table, headers=["ID", "Employee ID", "Start Date", "End Date", "Reason"]))
    else:
        print(f"No leaves found for employee ID {employee_id}")

def update_employee_helper():
    emp_id = int(input("Enter employee ID to update: "))
    name = input("Enter new name (leave blank to keep current): ")
    age = input("Enter new age (leave blank to keep current): ")
    department_id = input("Enter new department ID (leave blank to keep current): ")
    salary = input("Enter new salary (leave blank to keep current): ")

    conn = get_connection()
    update_employee(conn, emp_id, name=name if name else None, age=int(age) if age else None, department_id=int(department_id) if department_id else None, salary=int(salary) if salary else None)
    conn.close()
    print(f"Employee with ID {emp_id} updated.")

def update_department_helper():
    dept_id = int(input("Enter department ID to update: "))
    name = input("Enter new name (leave blank to keep current): ")
    description = input("Enter new description (leave blank to keep current): ")

    conn = get_connection()
    update_department(conn, dept_id, name=name if name else None, description=description if description else None)
    conn.close()
    print(f"Department with ID {dept_id} updated.")

def update_project_helper():
    project_id = int(input("Enter project ID to update: "))
    name = input("Enter new name (leave blank to keep current): ")
    description = input("Enter new description (leave blank to keep current): ")
    department_id = input("Enter new department ID (leave blank to keep current): ")

    conn = get_connection()
    update_project(conn, project_id, name=name if name else None, description=description if description else None, department_id=int(department_id) if department_id else None)
    conn.close()
    print(f"Project with ID {project_id} updated.")

def update_leave_helper():
    leave_id = int(input("Enter leave ID to update: "))
    employee_id = input("Enter new employee ID (leave blank to keep current): ")
    start_date = input("Enter new start date (YYYY-MM-DD) (leave blank to keep current): ")
    end_date = input("Enter new end date (YYYY-MM-DD) (leave blank to keep current): ")
    reason = input("Enter new reason (leave blank to keep current): ")

    conn = get_connection()
    update_leave(conn, leave_id, employee_id=int(employee_id) if employee_id else None, start_date=start_date if start_date else None, end_date=end_date if end_date else None, reason=reason if reason else None)
    conn.close()
    print(f"Leave with ID {leave_id} updated.")


def exit_program():
    print("Goodbye!")
    exit()
