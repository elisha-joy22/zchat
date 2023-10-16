from fastapi import FastAPI
from concurrent.futures import ThreadPoolExecutor
import grpc
import datetime

app = FastAPI()

#gRPC initialization
channel = grpc.insecure_channel("localhost:50051")
stub = "pass"

@app.post("/send_message")
async def sendmessage(username:str,text:str):
    message = f"{username}:{text}\n{datetime.datetime.now()}"
    print(message)
    return message    


 
