class HelloService:
    def __init__(self, hello_repo):
        self.hello_repo = hello_repo

    def get_hello(self):
        return self.hello_repo.get_message()
