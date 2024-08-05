import mysql.connector

def setup_tasks():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pratyusha",
        database="taskboard_db"
    )
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            task_number INT NOT NULL,
            task_name VARCHAR(255) NOT NULL,
            task_description TEXT,
            status ENUM('pending', 'in progress', 'completed') NOT NULL DEFAULT 'pending'
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("Tasks and Users tables created successfully.")

if __name__ == '__main__':
    setup_tasks()
