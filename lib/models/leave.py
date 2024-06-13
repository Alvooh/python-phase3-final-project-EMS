def create_leave(conn, employee_id, start_date, end_date, reason):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO leaves (employee_id, start_date, end_date, reason)
        VALUES (?, ?, ?, ?)
    ''', (employee_id, start_date, end_date, reason))
    conn.commit()

def get_leaves_by_employee(conn, employee_id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM leaves WHERE employee_id = ?', (employee_id,))
    return cursor.fetchall()


def update_leave(conn, leave_id, employee_id=None, start_date=None, end_date=None, reason=None):
    cursor = conn.cursor()
    if employee_id:
        cursor.execute('UPDATE leaves SET employee_id = ? WHERE id = ?', (employee_id, leave_id))
    if start_date:
        cursor.execute('UPDATE leaves SET start_date = ? WHERE id = ?', (start_date, leave_id))
    if end_date:
        cursor.execute('UPDATE leaves SET end_date = ? WHERE id = ?', (end_date, leave_id))
    if reason:
        cursor.execute('UPDATE leaves SET reason = ? WHERE id = ?', (reason, leave_id))
    conn.commit()
