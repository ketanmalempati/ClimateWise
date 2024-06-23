function addRow() {
    const table = document.getElementById('dataInput').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow(table.rows.length);
    newRow.insertCell(0).innerHTML = '<input type="date" name="date">';
    newRow.insertCell(1).innerHTML = '<input type="text" name="mode">';
    newRow.insertCell(2).innerHTML = '<input type="text" name="time">';
    newRow.insertCell(3).innerHTML = '<input type="text" name="distance">';
}

function submitData() {
    const table = document.getElementById('dataInput');
    const rows = Array.from(table.getElementsByTagName('tbody')[0].rows);
    const data = rows.map(row => {
        return {
            date: row.cells[0].getElementsByTagName('input')[0].value,
            mode: row.cells[1].getElementsByTagName('input')[0].value,
            time: row.cells[2].getElementsByTagName('input')[0].value,
            distance: row.cells[3].getElementsByTagName('input')[0].value
        };
    });

    fetch('/process-data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('results').textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => console.error('Error:', error));
}

// Initially add one empty row
window.onload = () => {
    addRow();
};
