'''You are asked to design a simple Payment System that can handle different payment methods.
Requirements:
Create a base class Payment with a method pay(amount).
Create three child classes that override the pay(amount) method:
CashPayment → print "Paid ₹<amount> in cash"
CardPayment → print "Paid ₹<amount> using credit/debit card"
UPIPayment → print "Paid ₹<amount> using UPI"
Task:
Create a list of payment objects (CashPayment, CardPayment, UPIPayment).
Loop through them and call pay(1000).
Each object should print a different message.
 '''
class Payment:
    def __init__(self,amount):
        self.amount=amount
    def payment(self):
        print("The amount is : ",self.amount)
        
class Cash(Payment):
    def payment(self):
        print(f"Paid ₹{self.amount} in cash")
    
    
class Credit(Payment):
    def payment(self):
        print(f"Paid ₹{self.amount} in credit card")
        
class UPI(Payment):
    def payment(self):
        print(f"Paid ₹{self.amount} in UPI mode")
        
list=[Cash(1000),Credit(1000),UPI(1000)]
for x in list:
    x.payment()