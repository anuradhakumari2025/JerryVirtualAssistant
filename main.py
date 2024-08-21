import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
  engine.say("I will speak this text")
  engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Love...")

# Reading Microphone as source
# Listening the speech and store in audio_text variable
# with sr.Microphone() as source:
#     print("Please say something")
#     audio_text = r.listen(source)
#     print("Time over, thanks")

#     try:
#         # Using google speech recognition
#         print("Text: " + r.recognize_google(audio_text))
#     except:
#         print("Sorry, I did not get that")
