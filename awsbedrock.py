# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 06:02:56 2024

@author: pruth
"""

# ------------------------------------------------- Code for resume and js and ques ---------------------------------

from flask import Flask, render_template, request, jsonify, session
import openai
import os
from groq import Groq
import boto3
import json
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

key = "sk-proj-GzMfyg5y5nDpiJwR2tPwT3BlbkFJUZGglPNm5xnBGqyUiEIt"
openai.api_key = key


# Groq_key = "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"
# client = Groq(
#     api_key=os.environ.get("Groq_key"),
# )

def generate_chat_response(resume, posting, previous_qa=[]):
    
    boto3.setup_default_session(aws_access_key_id="AKIA2UC3FUFD27GJ6K5D",
                                aws_secret_access_key="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",
                                region_name="us-east-1")

    bedrock_runtime = boto3.client(service_name='bedrock-runtime')

    model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'
    system_prompt = "you are given the content from a resume, and a job posting. generate a total of 7 strictly technical questions that test the applicant on requirements present on the job posting but are missing on the resume. These questions must test the applicant's knowledge and should not be generic. For example, instead of asking for 'Can you describe your experience in C++', you should ask 'Explain what C++ pointers are'. Essentially, the questions should test the candidate's technical skills. Separate each question with a delimiter '**--**'. return questions separated by the delimiter. Do not return or type anything else, as it causes problems when I parse the response."
    max_tokens = 4096

    # Prompt with user turn only.
    user_message =  {"role": "user", "content":"resume: " + resume + "\n\nJob posting: " + posting}
    assistant_message =  {"role": "assistant", "content": system_prompt}
    messages = [user_message, assistant_message]

    print("\n---------- message content \n",messages)
    body=json.dumps(
    {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": max_tokens,
        "messages": messages
    }  
)  


    response = bedrock_runtime.invoke_model(body=body, modelId=model_id)
    response_body = json.loads(response.get('body').read())

    # response_body
    results = response_body.get("content")[0].get("text")
    print("-----------------------------------------------------------------------------------",results)
    return results

   

def transcribe_met(audio_file_path):
    try:
        with open(audio_file_path, "rb") as audio_file:
            response = openai.Audio.transcribe("whisper-1", audio_file)
        transcription = response["text"]
        #     transcription_whisper = client.audio.transcriptions.create(file = "audio_file", model="whisper-large-v3") 
        # transcription = transcription_whisper["text"]
    except Exception as e:
        print(e)
        transcription = "Error."
    return transcription


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    resume = request.form.get('resume')
    posting = request.form.get('posting')
    user_answer = request.form.get('answer')

    if 'qa' not in session:
        session['qa'] = []

    previous_qa = session['qa']

    if user_answer:
        previous_question = previous_qa[-1]['question']
        previous_qa[-1]['answer'] = user_answer
        session['qa'] = previous_qa

    response = generate_chat_response(resume, posting, previous_qa)

    questions = response.split('**--**')
    new_question = questions[0].strip()

    session['qa'].append({'question': new_question, 'answer': ''})
    session.modified = True

    return jsonify({'question': new_question})

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio_file = request.files.get("audioFile")
    if not audio_file:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file_path = f"C:/Users/rahul/OneDrive/Desktop/InterviewBot/Audiofiles/{audio_file.filename}"
    audio_file.save(audio_file_path)

    transcript = transcribe_met(audio_file_path)
    print(transcript, "the data is here....................")
    return jsonify({'transcript': transcript})


if __name__ == "__main__":
    app.run(debug=False)
