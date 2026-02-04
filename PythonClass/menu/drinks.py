from PythonClass.menu.item_menu import item_menu

class drinks(item_menu):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return self._name
    
    def applicate_discount(self):
        self._price -= (self._price * 0.08)