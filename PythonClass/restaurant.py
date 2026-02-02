from PythonClass.avaluate import Avaluate

class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._avaluate = []
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self._name} | {self.category}"
    
    @classmethod
    def show_restaurants(cls):
        print(f"{"Restaurant name".ljust(25)} | {"Category".ljust(25)} | {"Status"}")
        for restaurant in cls.restaurants:
            print(f"{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {restaurant.active}")

    @property
    def active(self):
        return "☒" if self._active else "☐"
    
    def state_alternate(self):
        self._active = not self._active

    def receive_avaluate(self, client, note):
        avaluate = Avaluate(client, note)
        self._avaluate.append(avaluate)