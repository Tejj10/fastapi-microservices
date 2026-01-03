class HelloRepository:
    def __init__(self, db):
        self.db = db

    def get_message(self):
        return "Hello World"
