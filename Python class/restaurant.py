class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._active = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self.name} | {self.category}"
    
    def show_restaurants():
        print(f"{"Restaurant name".ljust(25)} | {"Category".ljust(25)} | {"Status"}")
        for restaurant in Restaurant.restaurants:
            print(f"{restaurant.name.ljust(25)} | {restaurant.category.ljust(25)} | {restaurant.active}")

    @property
    def active(self):
        return "☒" if self._active else "☐"

restaurant_rossi = Restaurant("rossi", "italian")
restaurant_vito = Restaurant("vito", "pizzeria")

Restaurant.show_restaurants()