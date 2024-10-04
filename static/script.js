function startRecording() {
    alert("Funcionalidad de grabación de audio en desarrollo.");
}

document.getElementById('task-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const taskText = document.getElementById('task').value;
    const [task, client, reminder] = parseTask(taskText);
    addTask(task, client, reminder);
});

function parseTask(text) {
    const task = text.match(/#tarea (.+?),/)[1];
    const client = text.match(/#cliente (.+?),/)[1];
    const reminder = text.match(/#recordatorio (.+)/)[1];
    return [task, client, reminder];
}

function addTask(task, client, reminder) {
    const table = document.getElementById('taskTable').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();
    newRow.insertCell(0).innerText = task;
    newRow.insertCell(1).innerText = client;
    newRow.insertCell(2).innerText = reminder;
}

function printPDF() {
    alert("Funcionalidad de imprimir en PDF en desarrollo.");
}
