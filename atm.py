
class Details:
    def __init__(self,CardNumber,PinNumber):
        self.CardNumber=CardNumber
        self.PinNumber=PinNumber
    
    def transaction(self,amount1):
        print(f"transaction done for rs.{amount1}")
        
    
    
    
cardNumber=input("your card number : ")
pin=input("your pin : ")
a=Details(cardNumber,pin)
amount=input("the amount needed")

a.transaction(amount)