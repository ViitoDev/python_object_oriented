from PythonClass.avaluate import Avaluate
from PythonClass.menu.item_menu import item_menu

class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._avaluate = []
        self._menu = []
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self._name} | {self.category}"
    
    @classmethod
    def show_restaurants(cls):
        print(f"{"Restaurant name".ljust(25)} | {"Category".ljust(25)} | {"Avaluate".ljust(25)} |{"Status"}")
        for restaurant in cls.restaurants:
            print(f"{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.restaurant_media).ljust(25)} |{restaurant.active}")

    @property
    def active(self):
        return "☒" if self._active else "☐"
    
    def state_alternate(self):
        self._active = not self._active

    def receive_avaluate(self, client, note):
        if 0 < note <= 5:
            avaluate = Avaluate(client, note)
            self._avaluate.append(avaluate)

    @property
    def restaurant_media(self):
        if not self._avaluate:
            return '-'
        notes_sum = sum(avaluate._note for avaluate in self._avaluate)
        notes_quantity = len(self._avaluate)
        media = round(notes_sum / notes_quantity, 1)
        return media
    
    def add_item_menu(self,item):
        if isinstance(item, item_menu):
            self._menu.append(item)

    @property
    def show_menu(self):
        print(f"Cardapio do restaurante {self._name}\n")
        for i,item in enumerate(self._menu, start=1):
            if hasattr(item, "description"):
                message_item = f"{i}. Name: {item._name} | Price:  R${item._price} | Descprition: {item.description}"
                print(message_item)
            else:
                message_drink = f"{i}. Name: {item._name} | Price:  R${item._price} | Size: {item.size}"
                print(message_drink)