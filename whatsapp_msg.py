
from datetime import datetime
from datetime import timedelta
import pywhatkit
import speak
import take_command
contact = {"ashish": "+916263343153",
           "abhijeet": "+919425146509", "papa": "+919752952515"}


def whatsappMsg():
    try:
        speak.speak("Please Tell Me The Recipient Name")
        to = take_command.takeCommanad().lower()

        speak.speak("What Message You Want To Sent")
        content = take_command.takeCommanad()
        for key in contact:
            if key == to:
                number = contact[key]
                break
        time_hour = int(datetime.now().strftime("%H"))
        time_min = int(
            (datetime.now()+timedelta(minutes=1, seconds=15)).strftime("%M"))
        pywhatkit.sendwhatmsg(number, content, time_hour, time_min)
    except Exception as e:
        print("Sorry This Message Would Not Be Send , Please Try Again ")
