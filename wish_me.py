
from datetime import datetime
from datetime import timedelta
import speak


def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak.speak(
            "Good Mornig , I'm Jarvis ,    I Am Here To Assist You  ,     For Waking Me , Say Hello")
    elif hour >= 12 and hour < 18:
        speak.speak(
            "Good Afternoon , I'm Jarvis ,    I Am Here To Assist You  ,     For Waking Me , Say Hello")
    else:
        speak.speak(
            "Good Evening , I'm Jarvis ,    I Am Here To Assist You  ,     For Waking Me , Say Hello")
