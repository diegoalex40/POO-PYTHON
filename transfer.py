from bank import Bank

class Transfer(Bank):
    
    def __init__(self, id, ammount, bank, identification, numberAccount):
        super().__init__(id, ammount, bank, identification, numberAccount)
        