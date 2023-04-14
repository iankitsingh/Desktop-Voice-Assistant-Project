import sqlite3
import speak
# connection=sqlite3.connect("memory.db")


def create_connection():
    connection = sqlite3.connect("memory.db")
    return connection

# ins='''  insert into jarvisdb (query,reply) VALUES ('who are you','i am jarvis , a desktop assistent') '''
# connection.execute(ins)
# connection.commit()


def fetch_query_and_reply():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM jarvisdb")

    return cursor.fetchall()


def delete_who_what_query_and_reply():
    connection = create_connection()
    cursor = connection.cursor()
    delete_who = 'DELETE FROM jarvisdb WHERE query="who"'
    delete_what = 'DELETE FROM jarvisdb WHERE query="what"'

    cursor.execute(delete_who)
    cursor.execute(delete_what)
    connection.commit()
    connection.close()


def insert_who_and_what_query_and_answer():
    connection = create_connection()
    cursor = connection.cursor()
    insert_who = "INSERT INTO jarvisdb(query,reply) VALUES('who','wolframalpha')"
    insert_what = "INSERT INTO jarvisdb(query,reply) VALUES('what','wolframalpha')"
    cursor.execute(insert_who)
    cursor.execute(insert_what)
    connection.commit()
    connection.close()


def insert_query_and_answer(query, answer):
    connection = create_connection()
    cursor = connection.cursor()
    insert = "INSERT INTO jarvisdb(query,reply) VALUES('" + \
        query+"','"+answer+"')"
    # ins= "INSERT INTO jarvisdb (query,reply) VALUES ('who are you','i am jarvis , a desktop assistent')"
    cursor.execute(insert)
    connection.commit()
    connection.close()


def reply_from_database(query):
    try:
        rows = fetch_query_and_reply()
        reply = " "
        for row in rows:
            if row[0].lower() in query.lower():
                return row[1]
                break
        return reply
    except Exception as e:
        # print(e)
        speak.speak("Sorry Something Went Wrong Please Try Again Letter")
# query = "what is your name"
# answer = "who are you"
# insert_query_and_answer(query,answer)
# answer = reply_from_database("who created you")
# print(answer)


insert_who_and_what_query_and_answer()
delete_who_what_query_and_reply()
insert_who_and_what_query_and_answer()
