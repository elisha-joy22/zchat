from datetime import datetime
from protofiles import chat_pb2_grpc,chat_pb2
from db import db_ops



class SendMessage(chat_pb2_grpc.SendMessageServicer):
    def CreateChat(self, request, context):
        payload = {
            "user1":request.user1.id,
            "user2":request.user2.id
        }
        chat_pb2.CreateChatRequest(user1=request.user1,user2=request.user2)
        try:
            response = db_ops.create_chat(payload)

            if response:
                return chat_pb2.Response(message=response)
            return chat_pb2.Response(message="Chat exists!")
        except:
            response = chat_pb2.Response(error="Failed-Totally")
            return response

    
    def SendMessage(self, request, context):
        payload = {
            "sender_id":request.sender_id,
            "receiver_id":request.receiver_id,
            "text":request.text
        }
        chat_pb2.Message(**payload)
        if payload.get("sender_id")==payload.get("receiver_id"):
            return chat_pb2.Response(error="Cant send message to yoursef")

        try:
            chat_id = db_ops.create_chat(
                {"user1":request.sender_id,
                 "user2":request.receiver_id})
            print(chat_id)
            payload["chat_id"]=chat_id
            response = db_ops.create_message(payload)
            print("dd")
            if response.get("error"):
                return chat_pb2.Response(error=response.get("error"))
            else:
                return chat_pb2.Response(message=response.get("message"))
            
        except Exception as e:
            print(e)
            response = chat_pb2.Response(error="message delivery failed")
            return response
    


class CreateUser(chat_pb2_grpc.CreateUserServicer):
    def CreateUser(self, request, context):
        payload = {
            "name":request.name,
            "email":request.email
        }
        user = chat_pb2.User(name=request.name,email=request.email)
        try:
            response = db_ops.create_user(payload)
        except:
            response = chat_pb2.UserCreated(confirmation="User creation failed!",user=user)
            return response
        if response:
            response = chat_pb2.UserCreated(confirmation="User created!",user=user)
        else:
            response = chat_pb2.UserCreated(confirmation="User exists!",user=user)
        return response