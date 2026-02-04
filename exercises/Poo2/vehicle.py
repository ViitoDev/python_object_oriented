class vehicle:
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model
        self._status = False
    
    def __str__(self):
        status = "Onn" if self._status else "off"
        return print(f"Brand: {self._brand}\nModel: {self._model}\nStatus: {status}")