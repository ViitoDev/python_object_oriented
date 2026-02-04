from abc import ABC, abstractmethod

class item_menu(ABC):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @abstractmethod
    def applicate_discount(self):
        pass