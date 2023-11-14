def create_wallet():
    username = input("Please set a username for your wallet")
    password = input("Please set a password for your wallet: ")
    confirm_password = input("Confirm your password: ")

   
    while password != confirm_password:
        print("Passwords do not match. Please try again.")
        password = input("Please set a password for your wallet: ")
        confirm_password = input("Confirm your password: ")

    
    print("Wallet created successfully!")
   

def login_to_wallet():
    username = input("Enter your wallet username")
    password = input("Enter your wallet password: ")

   
    correct_username = "parsaparsa"
    correct_password = "password123"  

    
    if password == correct_password and username == correct_username:
        print("Login successful!")
    
    else:
        print("Incorrect password. Please try again.")


print("Welcome to the Wallet Program!")


choice = input("(1) create a new wallet (2) login to an existing wallet? ")

if choice == "1":
    create_wallet()
elif choice == "2":
    login_to_wallet()
else:
    print("Invalid choice. Please try again.")







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

# parsa its the time bitch
