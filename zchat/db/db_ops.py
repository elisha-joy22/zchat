from datetime import datetime

from .db import db_connection_handler

@db_connection_handler
def create_user(user_data,cursor=None):
    name = user_data["name"]
    email = user_data["email"]

    # Check if a chat with the same user combination already exists (both ways)
    select_query = "SELECT id FROM users WHERE (email = %s)"
    data = (name, email)
    cursor.execute(select_query, data)
    existing_chat = cursor.fetchone()

    if existing_chat:
        # A chat with the same users already exists, you can handle this as needed
        print("User already exists with the same credentials!.")
        return False



    insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    data = (user_data['name'], user_data['email'])

    result = cursor.execute(insert_query, data)
    print("Data inserted successfully")
    return True



def check_chat_exists(user1,user2,cursor):
    # Check if a chat with the same user combination already exists (both ways)
    select_query = "SELECT id FROM chats WHERE (name = %s) OR (name=%s)"
    name1 = f"{user1}_{user2}"
    name2 = f"{user2}_{user1}"
    data = (name1,name2)
    cursor.execute(select_query, data)
    existing_chat = cursor.fetchone()
    return existing_chat[0] if existing_chat else None




@db_connection_handler
def create_chat(chatdata,cursor=None):
    user1 = chatdata['user1']
    user2 = chatdata['user2']
    chat_name = f"{user1}_{user2}"
    if user1==user2:
        return "Chat can't be created for a single user" 
    # Check if a chat with the same user combination already exists (both ways)
 
    chat_id = check_chat_exists(user1,user2,cursor)
    print(chat_id)
    if chat_id:
        print("chat exists",chat_id)
        return chat_id
    try:
        insert_query = "INSERT INTO chats (name,user1,user2) VALUES (%s, %s, %s)"
        data = (chat_name,user1,user2)
        cursor.execute(insert_query,data)
        chat_id = cursor.fetchone()[0]
        return chat_id
    except Exception as e:
        print("Error",e)
        return None


@db_connection_handler
def create_message(messagedata,cursor=None):
    sender_id = messagedata["sender_id"]
    receiver_id = messagedata["receiver_id"]
    message = messagedata["text"]
    timestamp = datetime.now()
    insert_query = "INSERT INTO messages (chat_id,sender_id,receiver_id,message,timestamp) VALUES (%s,%s,%s,%s,%s)"
    
    
    try:
        chat_id = create_chat({
                    "user1":sender_id,
                    "user2":receiver_id
        })
        data = (chat_id,sender_id,receiver_id,message,timestamp)
        print(data)
        result = cursor.execute(insert_query,data)
    except Exception as e:
        print(e)
        return {"error":"Message insertion failed!!"}
    
    return {"message":"Mesage inserted successfully"}
    