function sendMessage() {
    const inputField = document.getElementById('userInput');
    const chatbox = document.getElementById('chatbox');
    const userText = inputField.value.trim();

    if (userText === "") return;  // Prevent sending empty messages

    displayMessage(userText, 'client');
    inputField.value = '';  // Clear input field

    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({question: userText})
    })
    .then(response => response.json())
    .then(data => {
        displayMessage(data.response, 'server');
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function displayMessage(text, type) {
    const chatbox = document.getElementById('chatbox');
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message', type);
    msgDiv.textContent = text;
    chatbox.appendChild(msgDiv);
    chatbox.scrollTop = chatbox.scrollHeight;  // Auto scroll to the latest message
}
