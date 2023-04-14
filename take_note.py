import speech_recognition as sr
def takeCommanad():

    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("listening...")
        r.energy_threshold = 150
        r.pause_threshold = 2

        audio = r.listen(source, 0, 4)
    try:

        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")

        print(f"You Said: {query}\n")

    except Exception as e:
        print("Say That Again Please...!!")
        return "None"
    return query
