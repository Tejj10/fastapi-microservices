class HelloAPI:
    def __init__(self, hello_service):
        self.hello_service = hello_service

    def get_hello(self):
        return {"message": self.hello_service.get_hello()}
