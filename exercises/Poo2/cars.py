from vehicle import vehicle

class car(vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self._doors = doors

    def __str__(self):
        return f"Brand: {self._brand}\nModel: {self._model}\nDoors: {self._doors}"