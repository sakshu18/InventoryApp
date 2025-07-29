from db import get_connection
from auth import hash_password

conn = get_connection()
cursor = conn.cursor()

hashed = hash_password("123456")

cursor.execute("DELETE FROM users WHERE username = %s", ("admin",))
cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)",
               ("admin", hashed, "admin"))

conn.commit()
cursor.close()
conn.close()

print("✅ Admin inserted with password: 123456")
