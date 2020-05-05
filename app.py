from flask import Flask, render_template, request
import speech_recognition as sr
#import pyaudio

app = Flask(__name__)

r = sr.Recognizer()


def audio_text():
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            text = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
            # print(f"You said : {text}")
            return text
        except:
            return "Sorry could not recognize your voice"

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/predict", methods=['POST'])
def predict():
    print("predicted")
    if request.method == 'POST':
        model_prediction=audio_text()
        return render_template('home.html', prediction = model_prediction)

if __name__ == "__main__":
    #app.debug=True
    app.run()

 