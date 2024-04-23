import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    audio_data = r.record(source, duration=5)

print("Recognizing…")

# convert speech to text
text = r.recognize_google(audio_data, language='zh_cn')


print(text)