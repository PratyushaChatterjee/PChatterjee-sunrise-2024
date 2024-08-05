import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pratyusha",
        database="taskboard_db"
    )

def fetch_tasks():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks;")
    results = cursor.fetchall()
    for row in results:
        print(row)
    conn.close()

if __name__ == '__main__':
    fetch_tasks()
