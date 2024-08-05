document.addEventListener('DOMContentLoaded', () => {
    fetchTasks();

    document.getElementById('createTaskForm').addEventListener('submit', function(e) {
        e.preventDefault();
        createTask();
    });
});

function fetchTasks() {
    fetch('/tasks')
        .then(response => response.json())
        .then(tasks => {
            displayTasks(tasks, 'all-tasks');
            displayTasks(tasks.filter(task => task.status === 'pending'), 'pending-tasks');
            displayTasks(tasks.filter(task => task.status === 'in progress'), 'in-progress-tasks');
            displayTasks(tasks.filter(task => task.status === 'completed'), 'completed-tasks');
        });
}

function displayTasks(tasks, elementId) {
    const taskList = document.getElementById(elementId);
    taskList.innerHTML = '';
    tasks.forEach(task => {
        const taskItem = document.createElement('li');
        taskItem.className = 'list-group-item task';
        taskItem.textContent = `${task.task_number}: ${task.task_name}`;

        // Add dropdown to change status
        const statusDropdown = document.createElement('select');
        statusDropdown.innerHTML = `
            <option value="pending" ${task.status === 'pending' ? 'selected' : ''}>Pending</option>
            <option value="in progress" ${task.status === 'in progress' ? 'selected' : ''}>In Progress</option>
            <option value="completed" ${task.status === 'completed' ? 'selected' : ''}>Completed</option>
        `;
        statusDropdown.addEventListener('change', () => {
            updateTaskStatus(task.id, statusDropdown.value);
        });

        taskItem.appendChild(statusDropdown);
        taskList.appendChild(taskItem);
    });
}

function updateTaskStatus(taskId, newStatus) {
    fetch(`/tasks/${taskId}`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ status: newStatus })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        fetchTasks();
    });
}

function createTask() {
    const taskNumber = document.getElementById('taskNumber').value;
    const taskName = document.getElementById('taskName').value;
    const taskDescription = document.getElementById('taskDescription').value;
    const taskStatus = document.getElementById('taskStatus').value;

    fetch('/tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            task_number: taskNumber,
            task_name: taskName,
            task_description: taskDescription,
            status: taskStatus
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        fetchTasks();
        $('#createTaskModal').modal('hide');
        document.getElementById('createTaskForm').reset();
    });
}

