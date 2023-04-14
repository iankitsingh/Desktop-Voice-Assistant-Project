import wolframalpha
import os
import speak
import take_command
import database

api_id = os.environ['Wolframalpha_API']


def wolframalpha_search(query):
    try:
        client = wolframalpha.Client(api_id)
        response = client.query(query)
        output = str(next(response.results).text)
        return output

    except Exception as e:
        speak.speak(
            "I Don't Know This One , Can You Please Tell Me What It Means")
        answer = take_command.takeCommanad()
        if "no" in answer:
            speak.speak("OK , No Problem")
        elif "it means" in answer:
            answer = answer.replace("it means", "")
            answer = answer.strip()

            value = database.reply_from_database(answer)
            if value == " ":
                database.delete_who_what_query_and_reply()
                database.insert_query_and_answer(query, answer)
                speak.speak("Thank You For The Answer , I Will Remember It")
                database.insert_who_and_what_query_and_answer()
            else:
                database.delete_who_what_query_and_reply()
                database.insert_query_and_answer(query, value)
                speak.speak("Thank You For The Answer , I Will Remember It")
                database.insert_who_and_what_query_and_answer()
