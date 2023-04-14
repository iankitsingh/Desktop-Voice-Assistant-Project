from datetime import datetime
from datetime import timedelta
import wikipedia
import webbrowser
import os
import pywhatkit
import speak
import take_command
import wakeup
import whatsapp_msg
import wish_me
import weather
import database
import os
import wolframalpha_api
import take_note


def main_execution():
    try:

        con = database.create_connection()
        # wish_me.wishMe()

        while True:
            query = wakeup.wakeup().lower()
            if "hello" in query:
                speak.speak("How Can I Help You..")

                while True:
                    query = take_command.takeCommanad().lower()
                    reply = database.reply_from_database(query)

                    if "sleep" in reply:
                        speak.speak("Ok Sir , You Can Call Me Any Time")
                        break

                    elif "wikipedia" in reply:
                        speak.speak("searching wikipedia...")

                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        speak.speak("According To Wikipedia ")
                        print(results)
                        speak.speak(results)
                        break

                    elif "wolframalpha" in reply:
                        speak.speak("searching...")
                        query = query.replace("search", "")
                        query = query.strip()
                        response = wolframalpha_api.wolframalpha_search(query)
                        print(response)
                        speak.speak(response)
                        break

                    elif "open youtube" in reply:
                        speak.speak("Opening Youtube")
                        webbrowser.open("https://www.youtube.com/")
                        break

                    elif "close youtube" in reply:
                        speak.speak("Closing Youtube")
                        os.system("taskkill /f /im chrome.exe")
                        break

                    elif "open google" in reply:
                        speak.speak("Opening Google")
                        webbrowser.open("https://www.google.co.in/")
                        break

                    elif "close chrome" in reply:
                        speak.speak("Closing google chrome")
                        os.system("taskkill /f /im chrome.exe")
                        break

                    elif "search in google" in reply:
                        search = query.replace("search in google", "")
                        search = search.strip()
                        # print(search)
                        speak.speak("Searching In Google")
                        webbrowser.open(
                            "https://www.google.com/search?q="+search)
                        break

                    elif "open instagram" in reply:
                        speak.speak("Opening Instagram")
                        webbrowser.open("https://www.instagram.com/")
                        break

                    elif "close instagram" in reply:
                        speak.speak("Closing instagram")
                        os.system("taskkill /f /im chrome.exe")
                        break

                    elif "my attendance" in reply:
                        speak.speak("Opening Nh2 Webpage")
                        webbrowser.open("https://portal.aksuniversity.com/")
                        break

                    elif "close attendance" in reply:
                        speak.speak("Closing attendance")
                        os.system("taskkill /f /im chrome.exe")
                        break

                    elif "open whatsapp" in reply:
                        speak.speak("Opening Whatsapp")
                        webbrowser.open("https://web.whatsapp.com/")
                        break

                    elif "close whatsapp" in reply:
                        speak.speak("Closing whatsapp")
                        os.system("taskkill /f /im chrome.exe")
                        break

                    elif "time" in reply:
                        strTime = datetime.now().strftime("%H:%M:%S")
                        speak.speak(f"Sir,The Time Is {strTime}")
                        break

                    elif "open vs code" in reply:
                        speak.speak("Opening Visual Studio Code")
                        path = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                        os.startfile(path)
                        break

                    elif "close vs code" in reply:
                        speak.speak("Closing visual studio code")
                        os.system("taskkill /f /im Code.exe")
                        break

                    elif "open notepad" in reply:
                        speak.speak("Opening NotePad")
                        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
                        os.startfile(path)
                        break

                    elif "take a note" in reply:
                        speak.speak("What You Want To Note Down Sir")
                        note = take_command.takeCommanad()
                        f = open("test.txt",'w')
                        f = write(note)
                        f.close()
                        break



                    elif "close notepad" in reply:
                        speak.speak("Closing NotePad")
                        os.system("TASKKILL /F /im notepad.exe")
                        break

                    elif "open gmail" in reply:
                        speak.speak("Opening Gmail")
                        webbrowser.open(
                            "https://mail.google.com/mail/u/0/#inbox")
                        break

                    elif "close gmail" in reply:
                        speak.speak("Closing gmail")
                        os.system("taskkill /f /im chrome.exe")
                        break

                    elif "open database" in reply:
                        speak.speak("Opening Database")
                        path = "C:\\Program Files\\DB Browser for SQLite\\DB Browser for SQLite.exe"
                        os.startfile(path)
                        break

                    elif "close database" in reply:
                        speak.speak("Closing Database")
                        os.system("taskkill /f /im DB Browser for SQLite.exe")
                        break

                    elif "video" in reply:
                        video = query.replace("play", "")
                        speak.speak(f"playing")
                        pywhatkit.playonyt(video)
                        break

                    elif "song" in reply:
                        song = query.replace("play", "")
                        speak.speak(f"playing")
                        pywhatkit.playonyt(song)
                        break

                    elif "send whatsapp message" in reply:
                        whatsapp_msg.whatsappMsg()
                        break

                    elif "weather" in reply:
                        weather.weather()
                        break

                    elif "outside" in reply:
                        pass

                    elif "open control pannel" in reply:
                        speak.speak("Opening Control Pannel")
                        path = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk"
                        os.startfile(path)
                        break

                    elif "close control pannel" in reply:
                        speak.speak("Closing Control Pannel")
                        os.system("taskkill /f /im Taskmgr.exe")
                        break

                    elif "shutdown" in reply:
                        speak.speak(
                            "Do You Really Want To Shutdown Your Pc  ,   Please Make Sure All Your Current Work Has Been Saved")
                        confirmation = take_command.takeCommanad()
                        if "yes" in confirmation:
                            speak.speak("Shuting Down Your Pc")
                            os.system("shutdown /s /t 0")
                        else:
                            speak.speak("OK , No Problem")
                            break

                    elif "restart" in reply:
                        speak.speak(
                            "Do You Really Want To Restart Your Pc  ,   Please Make Sure All Your Current Work Has Been Saved")
                        confirmation = take_command.takeCommanad()
                        if "yes" in confirmation:
                            speak.speak("Restarting Your Pc")
                            os.system("shutdown /r /t 0")
                        else:
                            speak.speak("OK , No Problem")
                            break

                    elif "logoff" in reply:
                        speak.speak(
                            "Do You Really Want To Logoff Your Pc  ,   Please Make Sure All Your Current Work Has Been Saved")
                        confirmation = take_command.takeCommanad()
                        if "yes" in confirmation:
                            speak.speak("Logging Off Your Pc")
                            os.system("shutdown /l /t 0")
                        else:
                            speak.speak("OK , No Problem")
                            break

                    elif "exit" in reply:
                        speak.speak(
                            "Thank You For Using Me Sir!! Have A Good Day!!")
                        exit()
                        con.close()

                    else:
                        if "None" in query:
                            break

                        elif len(reply) > 1:
                            speak.speak(" "+reply)
                            break
                        else:
                            speak.speak(
                                "I Don't Know This One , Can You Please Tell Me What It Means")
                            answer = take_command.takeCommanad()
                            # reply = database.reply_from_database(answer)
                            if "no" in answer:
                                speak.speak("OK , No Problem")
                                break
                            elif "it means" in answer:
                                answer = answer.replace("it means", "")
                                answer = answer.strip()

                                value = database.reply_from_database(answer)
                                if value == " ":
                                    # database.create_connection()
                                    # ins="insert into jarvisdb values('"+query+"," +answer+"')"
                                    database.insert_query_and_answer(
                                        query, answer)
                                    speak.speak(
                                        "Thank You For The Answer , I Will Remember It")
                                    break
                                else:
                                    database.insert_query_and_answer(
                                        query, value)
                                    speak.speak(
                                        "Thank You For The Answer , I Will Remember It")
                                    break
                            elif "None" in answer:
                                speak.speak("Please Say That Again Please")
                                break

    except Exception as e:
        print(e)
        print("Something Went Wrong While Running Main Execution , Please Check Main Execution Module")
        speak.speak(
            "Something Went Wrong While Running Main Execution , Please Check Main Execution Module")
        main_execution()    


# main_execution()
