from fastapi import Depends
from app.api.hello_api import HelloAPI

def say_hello(api: HelloAPI = Depends()):
    return api.get_hello()
