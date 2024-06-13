def create_department(conn, name, description):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO departments (name, description)
        VALUES (?, ?)
    ''', (name, description))
    conn.commit()

def get_all_departments(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM departments')
    return cursor.fetchall()

def delete_department(conn, dept_id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM departments WHERE id = ?', (dept_id,))
    conn.commit()


def update_department(conn, dept_id, name=None, description=None):
    cursor = conn.cursor()
    if name:
        cursor.execute('UPDATE departments SET name = ? WHERE id = ?', (name, dept_id))
    if description:
        cursor.execute('UPDATE departments SET description = ? WHERE id = ?', (description, dept_id))
    conn.commit()
