def create_project(conn, name, description, department_id):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO projects (name, description, department_id)
        VALUES (?, ?, ?)
    ''', (name, description, department_id))
    conn.commit()

def get_all_projects(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects')
    return cursor.fetchall()

def delete_project(conn, project_id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM projects WHERE id=?', (project_id,))
    conn.commit()

def update_project(conn, project_id, name=None, description=None, department_id=None):
    cursor = conn.cursor()
    if name:
        cursor.execute('UPDATE projects SET name = ? WHERE id = ?', (name, project_id))
    if description:
        cursor.execute('UPDATE projects SET description = ? WHERE id = ?', (description, project_id))
    if department_id:
        cursor.execute('UPDATE projects SET department_id = ? WHERE id = ?', (department_id, project_id))
    conn.commit()
