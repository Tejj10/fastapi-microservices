class HelloAPI:
    def __init__(self, hello_service):
        self.hello_service = hello_service

    def get_hello(self):
        print("API CALLED")
        result = self.hello_service.get_hello()
        print("SERVICE RETURNED:", result)
        return {"message": result}
