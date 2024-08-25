import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import time

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
  engine.say(text)
  engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
       webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
       webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
       song = c.lower().split(" ")[1]
       musicLibrary.music[song]
       


if __name__ == "__main__":
    speak("Initializing Jerry...")
    # Reading Microphone as source
    # Listening the speech and store in audio_text variable
    while True:
      r= sr.Recognizer()
      print("recognising..")
      try:
          with sr.Microphone() as source:
            # Adjust for ambient noise and silence the recognition background noise
            r.adjust_for_ambient_noise(source, duration=1)
            # recognizer.energy_threshold = 300  # Lower this if the environment is quiet
            print("Listening...")
            speak("Please say something")

            # Listen for the first phrase and extract it into audio data
            audio = r.listen(source, timeout=8, phrase_time_limit=8)
      #     print("Recognising..")
      # Using google speech recognition
          word = recognizer.recognize_google(audio)
      #   print(f"Text: {command}")
      #   speak(f"You said: {command}") 
          if(word.lower() == "Jerry"):
            speak("ya")
            #Listen for command
            with sr.Microphone() as source:
                print("Jerry Active...")
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)

                processCommand(command)
  
      except sr.UnknownValueError:
        # Could not understand audio
        print("Sorry, I could not understand your speech.")
        speak("Sorry, I could not understand your speech.")

      except sr.RequestError as e:
        # Could not request results from Google Speech Recognition service
        print(f"Could not request results; {e}")
        speak("There was an error with the speech recognition service.") 

      except Exception as e:
      # Handle other exceptions
        print(f"Error: {e}")
        speak("There was an error.")

#   time.sleep(1)  # Add a short pause before the next iteration