import mysql.connector

# Database configuration
db_config = {
    'user': 'root',
    'password': 'Pratyusha',
    'host': 'localhost',
    'database': 'taskboard_db'
}

def create_tables():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    ''')

    # Create tasks table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task_number INT NOT NULL,
        task_name VARCHAR(255) NOT NULL,
        task_description TEXT NOT NULL,
        status ENUM('pending', 'in progress', 'completed') NOT NULL
    )
    ''')

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    create_tables()
