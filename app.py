from flask import Flask, request, jsonify, send_from_directory,render_template
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import io
import os
import openai
app = Flask(__name__, static_folder='static', template_folder='templates')

# Initialize the model and tokenizer
model_id = "vikhyatk/moondream2"
revision = "2024-05-20"
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True, revision=revision)
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/image_data')
def image_data():
    return render_template('index.html')
@app.route('/journal_data')
def journal_data():
    return render_template('jounal_index.html')

@app.route('/maps_data')
def maps_data():
    return render_template('maps_index.html')


@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        image = Image.open(io.BytesIO(file.read()))
        # enc_image = model.encode_image(image)
        # description = model.answer_question(enc_image, "Describe this image.", tokenizer)
        description = 'Welcome To Loves#392  02/24/24  17:12  Pump  Gallons Price  14  2.382  $4.199  Product  Amount  Unleaded  $ 10.00  TOTAL SALE $ 10.00  Card:  Cash  Sale  Manual  Ticket:  3116163  TOTAL SALE $ 10.00  DID YOU LOVE IT?  Tell us more at Loves.com/survey '
        
        print(description)
        return jsonify({'description':generate_chat_response(description) })
    
@app.route('/chat')
def chat():
    return render_template('chatbot_index.html')

# @app.route('/chatbots',method = ['POST'])
# def chatbots():
#     context = request.json['question']
#     return jsonify({'response': generate_chat_bot(context)})
    

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['question']
    # Here you simulate chatbot response logic.
    # For real implementation, integrate with an actual chatbot model.
    response = f"Echo: {question}"
    return jsonify({'response': generate_chat_bot(question)})

@app.route('/process-data', methods=['POST'])
def process_data():
    data = request.get_json()
    # Here you would normally call your LLM to process `data`
    # Simulating a response from an LLM with a simple transformation
    results = {entry['date']: entry for entry in data}
    s=""
    for i in list(results.keys()):
        s+=i+" "
        s+=" "+ str(results[i])
    # Return a JSON response with processed data
    return jsonify(generate_chat_response(s))

from flask import Flask, request, jsonify
import openai
import os

# app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/'
os.environ["OPENAI_API_KEY"] = 'sk-proj-GZp1yLEsq5M1mNMuiCDST3BlbkFJXO6r6V8AXsUNcxTuNh0V'
from openai import OpenAI
client = OpenAI()
# Assuming you have set your OpenAI API key elsewhere
openai.api_key = 'sk-proj-GzMfyg5y5nDpiJwR2tPwT3BlbkFJUZGglPNm5xnBGqyUiEIt'
def generate_chat_response(context, previous_qa=[],extra = ""):
    user_message = "user information: " + context
    system_message = """you are a climatologist whose main role is to calculate the carbon footprint based on daily tasks of users
    . you will be given a textual information of the daily expenditures, transportation,money spent on fuel,amount of fuel used, money spent on things that are not recyclable, journal data, based on these information if possible divide the 
    things into sub categories and give carbon impact on each of the category like cycling : -30kg, car 2 miles : +45kg,.... . always give in this exact format
    subcategory: impact in positive or negarive integer of kg each seperated by a comma ,if the data is not sufficient to infer from the context do not give a response 
    like this is not possible or i need extra information give an empty response that is important 
    . Also one final thing is give in few words how the user can offset the emission if the impact is negative
    , like grow 10 trees of this kind, prefer to walk this 2 kms of distance next time if possible, consider other alternative plans to offset the emissions.
    """+extra

    
    response = client.chat.completions.create(
      model="gpt-4",
      messages=[
          {
            "role": "system",
            "content": system_message
          },
        {
          "role": "user",
          "content": context
        }
      ],
      temperature=0,
      max_tokens=2024,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    ans = response.choices[0].message.content
    return ans
def generate_chat_bot(context, previous_qa=[],extra = ""):
    user_message = "user information: " + context
    system_message = """you are a climatologist whose main role is to calculate the carbon footprint based on daily tasks of users
    . you will be given a textual information of the daily expenditures, transportation,money spent on fuel,amount of fuel used, money spent on things that are not recyclable, journal data, based on these information if possible divide the 
    things into sub categories and give carbon impact on each of the category like cycling : -30kg, car 2 miles : +45kg,.... . always give in this exact format
    subcategory: impact in positive or negarive integer of kg each seperated by a comma ,you are also a bot who provide information related to carbon emission and climat impact given a context"""+extra

    
    response = client.chat.completions.create(
      model="gpt-4",
      messages=[
          {
            "role": "system",
            "content": system_message
          },
        {
          "role": "user",
          "content": context
        }
      ],
      temperature=0,
      max_tokens=2024,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    ans = response.choices[0].message.content
    return ans

provider = openai.OpenAI()
import os
from google.cloud import speech


def transcribe_audio_new(audio_file_path):
    # Set up the client
    # Set up the client
    client = speech.SpeechClient()

    # Load the audio file
    with open(audio_file_path, 'rb') as audio_file:
        content = audio_file.read()
    
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US'
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    # Print the transcriptions
    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))

    s=""
    for result in response.results:
        s+= 'Transcript: {}'.format(result.alternatives[0].transcript)
    return s

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    audio_file = request.files.get('audioFile')
    if audio_file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
        audio_file.save(filename)
        
        try:
            # with open(filename, "rb") as audio_file:
            #     response = openai.Audio.transcribe("whisper-1", audio_file)
            #     transcript = provider.audio.transcriptions.create(
            #         model="whisper-1", 
            #         file=audio_file, 
            #         response_format="text", language="en")
            # transcription = transcript
            #transcribe_audio_new(filename)
            pass
        except Exception as e:
            print(e)
            transcription = "Error."
        transcription = "Hi, i will be going to my firends place today thank i will be taking a cab to go dine outside by myself"
        print(transcription)
        
        # Process the transcript further if needed
        return jsonify({'transcript': generate_chat_response(transcription)})
        

    return jsonify({'error': 'No file received'}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5010)