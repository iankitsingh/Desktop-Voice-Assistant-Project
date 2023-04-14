import requests
import json
import os
from datetime import datetime
import speak
import take_command


def weather():
    api_key = os.environ['API_KEY']

    speak.speak("Please Say The City Name To Get Weather Details")
    query = take_command.takeCommanad()
    # query = input("city name\n")
    if query != "None":
        try:
            api_link = "https://api.openweathermap.org/data/2.5/weather?q="+query+"&appid="+api_key

            respons_obj = requests.get(api_link)
            api_data = respons_obj.json()

            # print(api_data)
            if api_data['cod'] == '404':
                speak.speak("Please Check City Name And Try Again")
            else:
                temp_city = ((api_data['main']['temp']) - 273.15)
                weather_description = api_data['weather'][0]['description']
                humidity = api_data['main']['humidity']
                wind_speed = api_data['wind']['speed']
                date_time = datetime.now().strftime("%H:%M:%S")

                print(f"Current Temperature Is :{int(temp_city)} cel")
                print(f"Current Weather Description :{weather_description}")
                print(f"Current Humidity :{humidity} %")
                print(f"Current Wind Speed :{wind_speed} KMPH")

                speak.speak("Current Temperature Is" +
                            str(int(temp_city))+"degree celcius")
                speak.speak("Current Weather Description" +
                            str(weather_description))
                speak.speak("Current Humidity"+str(humidity)+"Percent")
                speak.speak("Current Wind Speed" +
                            str(wind_speed)+"Kilo Meter Per Hours")
        except Exception as e:
            print(e)
            Speak.speak(
                "Sorry Due To Server Issue Can Not Get Data Please Try Again")
    else:
        speak.speak("Sorry I Didn't Understand Please Say That Again Please")
