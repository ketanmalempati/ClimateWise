from flask import Flask, request, jsonify, send_from_directory
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import io
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Initialize the model and tokenizer
model_id = "vikhyatk/moondream2"
revision = "2024-05-20"
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True, revision=revision)
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')

@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        image = Image.open(io.BytesIO(file.read()))
        enc_image = model.encode_image(image)
        description = model.answer_question(enc_image, "Describe this image.", tokenizer)
        return jsonify({'description': description})
    
@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['question']
    # Here you simulate chatbot response logic.
    # For real implementation, integrate with an actual chatbot model.
    response = f"Echo: {question}"
    return jsonify({'response': response})

@app.route('/process-data', methods=['POST'])
def process_data():
    data = request.get_json()
    # Here you would normally call your LLM to process `data`
    # Simulating a response from an LLM with a simple transformation
    results = {entry['date']: entry for entry in data}
    # Return a JSON response with processed data
    return jsonify(results)

from flask import Flask, request, jsonify
import openai
import os

# app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Assuming you have set your OpenAI API key elsewhere
openai.api_key = 'sk-proj-GzMfyg5y5nDpiJwR2tPwT3BlbkFJUZGglPNm5xnBGqyUiEIt'

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    audio_file = request.files.get('audioFile')
    if audio_file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
        audio_file.save(filename)
        
        # Transcribe using OpenAI's Whisper model (you'll need to set this up)
        transcript = openai.Audio.transcription.create(
            model="whisper-1",
            file=open(filename, "rb"),
            language="en"
        )
        
        # Process the transcript further if needed
        
        return jsonify({'transcript': transcript['text']})

    return jsonify({'error': 'No file received'}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5010)