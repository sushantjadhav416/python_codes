class Medicine:
    def __init__(self,mediName,batch,disease,price):
        self.mediName=mediName
        self.batch=batch
        self.disease=disease
        self.price=price
        
class solution:
    @classmethod 
    def getPriceByDisease(cls,List_medicen,dis):
        result=[]
        for i in List_medicen:
            if i.disease.lower() == dis.lower():
                result.append(i.price)
        return result   

if __name__=="__main__":
    n=int(input())
    List_medicen=[]
    for i in range(n):
        mediName=input()
        batch=input()
        disease=input()
        price=int(input())
        List_medicen.append(Medicine(mediName,batch, disease,price))
    
    dis=input()
    ans=solution.getPriceByDisease(List_medicen,dis)
    print("!!!!The required output!!!!")
    for i in ans:
        print(i)
    
    




