import os

import grpc
from concurrent import futures
from protofiles import chat_pb2_grpc
from services.services import SendMessage,CreateUser
from db.db import initialize_db


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_SendMessageServicer_to_server(SendMessage(),server)
    chat_pb2_grpc.add_CreateUserServicer_to_server(CreateUser(),server)

    server.add_insecure_port(f"[::]:{os.environ.get('GRPC_SERVER_PORT')}")
    print(f"Server listening on port {os.environ.get('GRPC_SERVER_PORT')}...")
    server.start()
    server.wait_for_termination()
    print("Server connection closed!")


if __name__=="__main__":
    initialize_db()
    serve()
    