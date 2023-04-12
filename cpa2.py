class account:
    def __init__(self,cardNum,pin,balance,witdrawAmt,Actyp):
        self.cardNum = cardNum
        self.pin = pin
        self.balance = balance
        self.witdrawAmt  =  witdrawAmt
        self.Actyp = Actyp
    
    def witdrawAmt(self):
        if self.witdrawAmt< = self.balance:
            self.balance=self.balance-self.witdrawAmt
        LIST=[]
        LIST.append(self.pin)
        LIST.append(self.balance)
        LIST.append(self.witdrawAmt)
        
        return LIST

class Atm(account):
    def __init__(self,CardNum,Pin,WitdrawAmt,Actyp):
        self.CardNum=cardNum
        self.Pin=pin
        self.WitdrawAmt=witdrawAmt
        self.Actyp=Actyp
    
    def updated_balance(self):
        if((self.cardNum != self.CardNum) and (self.pin != self.Pin) and (self.witdrawAmt != self.WitdrawAmt) and (self.actyp != self.Actyp)):
              return "No account Exists"
    
    
if __name__=="__main__": 
 n=int(input())
 List=[]
 for i in range(n):
    cardNum=int(input())
    pin=int(input())
    balance=float(input())
    witdrawAmt=float(input())
    Actyp=input()
    List.append(account(cardNum,pin,witdrawAmt,balance,Actyp))

 for i in range(1):
    cardNum=int(input())
    pin=int(input())
    witdrawAmt=float(input())
    Actyp=input()


