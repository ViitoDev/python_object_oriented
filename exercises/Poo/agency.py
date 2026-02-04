from exercises.Poo.bank import bank

class agency(bank):
    def __init__(self, name, number):
        super.__init__(name)
        self._number = number