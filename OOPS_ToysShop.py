class Toy :
    def __init__(self,Tid,Ttype,Tprice):
        self.Tid=Tid
        self.Ttype=Ttype
        self.Tprice=Tprice
        self.discount=0

class store:
    def __init__(self,Tlist,Typlist):
        self.Tlist=Tlist
        self.Typlist=Typlist
    
    def fun(self):
        for i in Tlist:
            if i.toyTypes.lower() in self.Typlist.lower():
                r=Typlist[i.Ttype.lower()]
                dis=i.price*(r/100)
                i.discount=dis




if __name__=="__main__":
    n=int(input())
    toys=[]
    toyTypes=[]
    for i in range(n):
      Tid=int(input())
      Ttyp=input()
      Tprice=int(input())
      toys.append(Toy(Tid,Ttyp,Tprice))
    
    for i in range(3):
        ttype=input()
        amount=int(input())
        toyTypes[ttype.lower()]=amount
    
    S=store(toys,toyTypes)
    S.fun()
    S.Tlist.sort(key=lambda x:x.discount,reverse = True)
    for i in S.Tlist:
        dp= i.price - i.discount
        print(i.id,i.price,dp)
    




    










