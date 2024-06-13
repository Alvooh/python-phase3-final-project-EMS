def create_employee(conn, name, age, department_id, salary):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO employees (name, age, department_id, salary)
        VALUES (?, ?, ?, ?)
    ''', (name, age, department_id, salary))
    conn.commit()

def get_all_employees(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    return cursor.fetchall()

def get_employees_by_department(conn, department_id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees WHERE department_id = ?', (department_id,))
    return cursor.fetchall()

def delete_employee(conn, emp_id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id = ?', (emp_id,))
    conn.commit()

def get_employee_by_id(conn, emp_id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees WHERE id = ?', (emp_id,))
    return cursor.fetchone()

def update_employee(conn, emp_id, name=None, age=None, department_id=None, salary=None):
    cursor = conn.cursor()
    if name:
        cursor.execute('UPDATE employees SET name = ? WHERE id = ?', (name, emp_id))
    if age:
        cursor.execute('UPDATE employees SET age = ? WHERE id = ?', (age, emp_id))
    if department_id:
        cursor.execute('UPDATE employees SET department_id = ? WHERE id = ?', (department_id, emp_id))
    if salary:
        cursor.execute('UPDATE employees SET salary = ? WHERE id = ?', (salary, emp_id))
    conn.commit()

