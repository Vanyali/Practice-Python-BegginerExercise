class BankAccount:
    counter = 0

    def __init__(self):
        BankAccount.counter += 1
        self.balance = 0
        self.accountNumber = 0


    def CreateAccount(self, balance):
        self.balance = balance
        self.accountNumber = BankAccount.counter

    
    def get_Account_Balance(self):
        return self.balance

    def get_Account_Number(self):
        return self.accountNumber

    def deposit(self, amount):
        self.balance += amount

    def check_minimum_balance(self, amount):
        if self.balance-amount < 100:
            return False
        else:
            return True

    def withdraw(self, amount):
        if self.check_minimum_balance(amount):
            self.balance -= amount
        else:
            print("You have very low balance you cant withdraw anything!")

print("**********WELCOME TO SOLO BANK*********")
print("\n")
print("Services We Provide:\n")
print("1.Create a Bank Account with some Initial balance.\n")
print("2.Deposit Amount to your account.\n")
print("3.Withdraw Amount from your account while maintaining a minimum of 500 in your account.\n")
print("4.Check your Balance.\n")
print("5.Check you Account number which is generated automatically.\n")

customer1 = BankAccount()
customer1.CreateAccount(3000)

print("Customer 1 Has Successfully Created a Bank Account.\nThe Initial Balance :",customer1.get_Account_Balance())
print("Account Number :",customer1.get_Account_Number())
print("----Depositing 5000 to account.----")
customer1.deposit(5000)
print("Amount Balance:",customer1.get_Account_Balance())
print("----Withdrawing 2000 from account.----")
customer1.withdraw(2000)
print("Current Balancing: ", customer1.get_Account_Balance())


