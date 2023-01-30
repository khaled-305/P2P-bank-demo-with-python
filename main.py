class User():
    def __init__(self, name):
        self.name = name

    def display_user_details(self):
        print('Customers details')
        print("Name ", self.name)

class Bank(User):
    def __init__(self, name):
        super().__init__(name)

        self.balance = 0

    def deposite(self, amount):
        self.amount = amount

        self.balance = self.balance + self.amount
        print("Deposite successful!")
        print("Current balance: $", self.balance)

    def withdraw(self, amount):
        self.amount = amount

        if self.balance < self.amount:
            print("Insufficient funds!")
            print("Your current balance is: $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Withdrawal of : $", self.amount , " was successful!")
            print("Your current balance is: $", self.balance)

    def check_balance(self):
        print("Your current balance is: $", self.balance)

    def transfer(self, receiver, amount):
        self.withdraw(amount)
        receiver.deposite(amount)

