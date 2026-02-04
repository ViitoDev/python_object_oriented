from PythonClass.menu.item_menu import item_menu

class item(item_menu):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description

    def __str__(self):
        return self._name
    
    def applicate_discount(self):
        self._price -= (self._price * 0.05)