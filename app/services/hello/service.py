class HelloService:
    def __init__(self, repo):
        self.repo = repo

    def get_hello(self):
        return self.repo.get_message()
