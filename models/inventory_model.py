from db import get_connection

def get_inventory():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM inventory")
    inventory = cursor.fetchall()
    conn.close()
    return inventory