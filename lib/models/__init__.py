import sqlite3

DATABASE_URL = "employees.db"

def get_connection():
    conn = sqlite3.connect(DATABASE_URL)
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            description TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            department_id INTEGER,
            salary INTEGER,
            FOREIGN KEY (department_id) REFERENCES departments(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            department_id INTEGER,
            FOREIGN KEY (department_id) REFERENCES departments(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leaves (
            id INTEGER PRIMARY KEY,
            employee_id INTEGER,
            start_date TEXT,
            end_date TEXT,
            reason TEXT,
            FOREIGN KEY (employee_id) REFERENCES employees(id)
        )
    ''')
    conn.commit()
    conn.close()
