class persons:
    def __init__(self, name="", age=0, profission=""):
        self.name = name
        self.age = age
        self.profission = profission

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nProfission: {self.profission}"
        
    @property
    def saudation(self):
        if self.profission:
            return f"Hello my name is {self.name}! I work as {self.profission}"
        else:
            return f"Hello my name is {self.name}!"
        
    def aniversary(self):
        self.age += 1