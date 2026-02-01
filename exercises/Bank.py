class bank_account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
        self._active = False
    
    def __self__(self):
        return f"Holder: {self.holder}\nBalance: {self.balance}"
    
    def activate_account(self):
        self._active = True

account1 = bank_account("Annelise", 2000)
account2 = bank_account("Rossi", 0)

print(f"Before activate: active account? {account1._active}")
account1.activate_account()
print(f"After activate: active account? {account1._active}")