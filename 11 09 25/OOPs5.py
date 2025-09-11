class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print(f"{amount} debited succesfully.")
    def withdraw(self,amount):
        if(self.__balance>=amount):
            self.__balance-=amount
            print(f"Amount {amount} withdraw successful.")
        else:
            print("Insufficient amount")
    def get_balance(self):
        return self.__balance
    
class BankAcc(BankAccount):
    def display(self):
        return self.__balance
    
a1=BankAccount(0)
a2=BankAcc(0)
a1.deposit(100000)
a1.withdraw(50000)
print("Balance amount:",a1.get_balance())    
print("BankAcc balance: ",a2.display()) 