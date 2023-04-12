class Blood:
    def __init__(self,bloodgroup,unitnhand):
        self.bloodgroup=bloodgroup
        self.unitnhand=unitnhand
    
class bloodbank:
    def __init__(self,b_list):
          self.b_list=b_list
    
    def isavailable(self,reqbd,unit):
        for i in b_list:
            if(i.bloodgroup==reqbd):
                if(i.unitnhand>=unit):
                   print("Blood is available!!!")
                   return
        print("Blood is not available!!!")
    
    def minbstack(self):
        mini=99999999
        for i in b_list:
            if(i.unitnhand<mini):
               mini=i.unitnhand
        for i in b_list:
            if(i.unitnhand==mini):
                print(i.bloodgroup)
      


if __name__=="__main__":
 n=int(input())
 b_list=[]
 for i in range(n):
    Bloodgroup=input("Enter a blood group:").upper()
    unitnhand=int(input("Enter a unit present:"))
    b_list.append(Blood(Bloodgroup,unitnhand))

 reqbd=input().upper()
 unit=int(input())
 bloodb1=bloodbank(b_list)
 bloodb1.isavailable(reqbd,unit)
 bloodb1.minbstack()

