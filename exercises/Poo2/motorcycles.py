from vehicle import vehicle

class motorcycle(vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self._type = type

    def __str__(self):
        return f"Brand: {self._brand}\nModel: {self._model}\nStatus: {self._status}"