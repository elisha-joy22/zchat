

from protofiles import chat_pb2_grpc,chat_pb2


def create_user(channel,payload):
    CreateUserStub = chat_pb2_grpc.CreateUserStub(channel)
    user_create_response = CreateUserStub.CreateUser(chat_pb2.User(
        **payload
    ))
    print(user_create_response)


def create_chat(channel,id1,id2):
    SendMessageStub = chat_pb2_grpc.SendMessageStub(channel)
    create_chat_response = SendMessageStub.CreateChat(chat_pb2.CreateChatRequest(
        user1=chat_pb2.User(id=id1),user2=chat_pb2.User(id=id2)
    ))
    print(create_chat_response)

def send_message(channel,payload):
    SendMessageStub = chat_pb2_grpc.SendMessageStub(channel)
    send_message_response = SendMessageStub.SendMessage(chat_pb2.Message(
        **payload
    ))
    print(send_message_response)