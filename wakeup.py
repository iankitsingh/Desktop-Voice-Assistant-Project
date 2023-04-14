
import speech_recognition as sr
# import speak


def wakeup():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 300
        r.pause_threshold = 2
        print("For Waking Me Up Say 'Hello'")

        audio = r.listen(source, 0, 5)
    try:

        query = r.recognize_google(audio, language="en-in")

        # print(f"You Said: {query}\n")
        if "hello" not in query:
            # print("Say That Again Please")
            pass

    except Exception as e:
        # speak.speak("Sorry Something Went Wrong Please Try Again")
        return "None"
    return query
