class restaurant:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False

restaurant_rossi = restaurant("rossi", "italian")
restaurant_vito = restaurant("vito", "pizzeria")

restaurants = [restaurant_rossi, restaurant_vito]
print(vars(restaurant_rossi))