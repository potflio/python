import pyttsx3

engine = pyttsx3.init()

text = "my name is jarvis"

engine.say(text)

engine.runAndWait()