document.getElementById('uploadForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData();
    const imageInput = document.getElementById('imageInput');
    const imageDescription = document.getElementById('imageDescription');

    if (imageInput.files.length > 0) {
        formData.append('file', imageInput.files[0]);
        fetch('/upload-image', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if(data.description) {
                imageDescription.textContent = `Description: ${data.description}`;
            } else {
                imageDescription.textContent = 'Error: Could not generate a description.';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            imageDescription.textContent = 'Error: Failed to connect to server.';
        });
    } else {
        imageDescription.textContent = 'Please select an image file.';
    }
});
