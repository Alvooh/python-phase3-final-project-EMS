from helpers import (
    add_employee,
    view_employees,
    view_employees_by_department,
    delete_employee_helper,
    add_department,
    view_departments,
    delete_department_helper,
    add_project,
    view_projects,
    delete_project_helper,
    add_leave,
    view_employee_leaves,
    update_employee_helper,
    update_department_helper,
    update_project_helper,
    update_leave_helper,
    view_employee_by_id,
    exit_program
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            view_employees_by_department()
        elif choice == "4":
            delete_employee_helper()
        elif choice == "5":
            add_department()
        elif choice == "6":
            view_departments()
        elif choice == "7":
            delete_department_helper()
        elif choice == "8":
            add_project()
        elif choice == "9":
            view_projects()
        elif choice == "10":
            delete_project_helper()
        elif choice == "11":
            add_leave()
        elif choice == "12":
            view_employee_leaves()
        elif choice == "13":
            update_employee_helper()
        elif choice == "14":
            update_department_helper()
        elif choice == "15":
            update_project_helper()
        elif choice == "16":
            update_leave_helper()
        elif choice == "17":
            view_employee_by_id()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a new employee")
    print("2. View all employees")
    print("3. View employees by department")
    print("4. Delete an employee")
    print("5. Add a new department")
    print("6. View all departments")
    print("7. Delete a department")
    print("8. Add a new project")
    print("9. View all projects")
    print("10. Delete a project")
    print("11. Add a leave for an employee")
    print("12. View leaves for an employee")
    print("13. Update an employee")
    print("14. Update a department")
    print("15. Update a project")
    print("16. Update a leave")
    print("17. Get employee by ID")

if __name__ == "__main__":
    main()
