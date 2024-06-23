let isRecording = false;
let mediaRecorder;
let recordedChunks = [];
const audioPreview = document.getElementById('audioPreview');
const responseAudio = document.getElementById('responseAudio');
const startButton = document.getElementById('startButton');
const stopButton = document.getElementById('stopButton');
const transcriptContainer = document.getElementById('transcriptContainer');

startButton.addEventListener('click', async () => {
  if (!isRecording) {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    audioPreview.srcObject = stream;
    audioPreview.muted = true;

    mediaRecorder = new MediaRecorder(stream);
    recordedChunks = [];

    mediaRecorder.ondataavailable = (event) => {
      if (event.data.size > 0) {
        recordedChunks.push(event.data);
      }
    };

    mediaRecorder.onstop = () => {
      const audioBlob = new Blob(recordedChunks, { type: 'audio/webm' });
      sendAudioToServer(audioBlob);
    };

    mediaRecorder.start();
    audioPreview.style.display = 'block';
    responseAudio.style.display = 'none';
    startButton.disabled = true;
    stopButton.disabled = false;
    isRecording = true;
  }
});

stopButton.addEventListener('click', () => {
  if (isRecording) {
    mediaRecorder.stop();
    audioPreview.srcObject.getTracks().forEach(track => track.stop());
    startButton.disabled = false;
    stopButton.disabled = true;
    isRecording = false;
  }
});

function sendAudioToServer(audioBlob) {
  const formData = new FormData();
  formData.append("audioFile", audioBlob, "recorded-audio.webm");

  fetch("/transcribe", {
    method: "POST",
    body: formData,
  })
  .then(response => response.json())
  .then(data => {
    const transcript = data.transcript;
    transcriptContainer.innerText = transcript;
    transcriptContainer.style.display = 'block';
  })
  .catch((error) => {
    console.error("Error sending audio to server:", error);
  });
}
