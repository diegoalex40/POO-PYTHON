from account import Account

class Driver(Account):
    id      = int
    license = str
    
    def __init__(self, id, license, name, document, mail, password, gender, numberCell, age):
        super().__init__(name, document, mail, password, gender, numberCell, age)
        self.id         = id
        self.license    = license