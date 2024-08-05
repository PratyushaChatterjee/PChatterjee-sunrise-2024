from flask import Flask, jsonify, request, send_from_directory
import mysql.connector

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

# Database configuration
db_config = {
    'user': 'root',
    'password': 'Pratyusha',
    'host': 'localhost',
    'database': 'taskboard_db'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return jsonify(tasks)

@app.route('/tasks/in-progress', methods=['GET'])
def get_in_progress_tasks():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tasks WHERE status = "in progress"')
    tasks = cursor.fetchall()
    conn.close()
    return jsonify(tasks)

@app.route('/tasks/completed', methods=['GET'])
def get_completed_tasks():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tasks WHERE status = "completed"')
    tasks = cursor.fetchall()
    conn.close()
    return jsonify(tasks)

@app.route('/tasks/pending', methods=['GET'])
def get_pending_tasks():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tasks WHERE status = "pending"')
    tasks = cursor.fetchall()
    conn.close()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task_number, task_name, task_description, status) VALUES (%s, %s, %s, %s)',
                   (new_task['task_number'], new_task['task_name'], new_task['task_description'], new_task['status']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task created successfully'}), 201

@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task_status(task_id):
    new_status = request.json['status']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = %s WHERE id = %s', (new_status, task_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task status updated successfully'})

if __name__ == '__main__':
    app.run(debug=True)


