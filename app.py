from flask import Flask, request, send_file, render_template, url_for, redirect
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    action_type = request.form['action_type']
    language = 'en'
    
    # Create a gTTS object
    speech = gTTS(text=text, lang=language, slow=False)
    
    # Save the converted audio to a file
    audio_file = "static/output.mp3"
    speech.save(audio_file)
    
    # Generate the URL for the audio file
    audio_url = url_for('static', filename='output.mp3')
    
    if action_type == 'live':
        # Render the template with the audio URL to play live
        return render_template('index.html', audio_url=audio_url)
    elif action_type == 'download':
        # Redirect to the download route
        return redirect(url_for('download'))

@app.route('/download')
def download():
    return send_file('static/output.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
