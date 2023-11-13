class Wallet:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"DEPOSITED {amount}. BALANCE: {self.balance}.")
        else:
            print("INAVLID!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"WITHDREW {amount}. BALANCE: {self.balance}.")
        elif amount <= 0:
            print("INVALID!")
        else:
            print("INSUFFICIENT!")

class Human(Wallet):
    def __init__(self):
        super().__init__()

    def put_money(self, amount):
        if amount > 0:
            self.deposit(amount)
        else:
            print("INVALID!")

    def take_money(self, amount):
        if amount > 0 and amount <= self.balance:
            self.withdraw(amount)
        elif amount <=0:
            print("INVALID!")
        else:
            print("INSUFFICIENT!")

class Machine(Wallet):
    def __init__(self):
        super().__init__()



    def process_payment(self, amount):
        if amount > 0 and amount <= self.balance:
            self.withdraw(amount)
        elif amount <= 0:
            print("INVALID!")
        else:
            print("INSUFFICIENT!")
            #parsa code
            
