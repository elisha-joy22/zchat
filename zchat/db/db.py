from dotenv import load_dotenv

import os
import psycopg2

load_dotenv()

db_params = {
        "dbname":os.environ.get("DB_NAME"),
        "user":os.environ.get("DB_USER"),
        "password":os.environ.get("DB_PASSWORD"),
        "host":os.environ.get("DB_HOST"),
        "port":os.environ.get("DB_PORT")
    }

print(db_params)
def initialize_db():    
    #connection
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    create_user_table = """
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(255)
        );
    """
    create_chat_table = """
        CREATE TABLE IF NOT EXISTS chats(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            user1 INT REFERENCES users(id),
            user2 INT REFERENCES users(id)
        );
    """
    create_message_table = """
        CREATE TABLE IF NOT EXISTS messages(
            id SERIAL PRIMARY KEY,
            chat_id INT REFERENCES chats(id),
            sender_id INT REFERENCES users(id),
            receiver_id INT REFERENCES users(id),
            message TEXT,
            timestamp TIMESTAMP  
        );
    """
    cursor.execute(create_user_table)
    result = connection.commit()
    cursor.execute(create_chat_table)
    result = connection.commit()
    cursor.execute(create_message_table)
    result = connection.commit()


    #connection close
    cursor.close()
    connection.close()


def db_connection_handler(func):
    def wrapper(*args,**kwargs):
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()
        result = func(*args,**kwargs,cursor=cursor)

        connection.commit()
        cursor.close()
        connection.close()
        return result
    return wrapper


