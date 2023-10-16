import grpc
from client.client_functions import create_user,create_chat,send_message
from protofiles.chat_pb2 import User


create_user_payload = {
    "name":"User",
    "email":"user@gmail.com"
}

create_chat_payload = {
    "user1":3,
    "user2":3,
}

send_message_payload = {
    "sender_id":2,
    "receiver_id":3,
    "text":"Your text"
}

def run():
    channel = grpc.insecure_channel("localhost:5001")
    #create_user(channel,create_user_payload)
    #create_chat(channel,create_chat_payload["user1"],create_chat_payload["user2"])
    send_message(channel,send_message_payload)



if __name__ =="__main__":
    run()
