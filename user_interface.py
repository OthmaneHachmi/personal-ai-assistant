from text_generation import *
from flask import Flask, request, render_template

personal_assistant = PersonalAssistant()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.form['prompt']
    response = personal_assistant.text_genertion(prompt)
    return render_template('index.html', response=response)


if __name__ == '__main__':
    app.run(debug=True)