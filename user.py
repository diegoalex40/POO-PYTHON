from account import Account

class User(Account):
    id = int
    
    def __init__(self, id, name, document, mail, password, gender, numberCell, age):
        super().__init__(name, document, mail, password, gender, numberCell, age)
        self.id    = id