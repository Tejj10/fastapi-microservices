from fastapi import FastAPI
import requests

app = FastAPI()

HELLO_SERVICE_URL = "http://localhost:8001/hello"

@app.get("/say-hello")
def say_hello():
    response = requests.get(HELLO_SERVICE_URL)
    return response.json()
