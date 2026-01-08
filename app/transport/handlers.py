from fastapi import Depends
from app.api.hello_api import HelloAPI

def say_hello(api: HelloAPI = Depends()):
    print("HANDLER CALLED")
    return api.get_hello()
