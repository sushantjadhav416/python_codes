def RotateByone(List):
    last=List[-1]
    for i in reversed(range(len(List)-1)):
        List[i+1]=List[i]
    List[0]=last
def Rotate(List,k):
    for i in range(k):
        RotateByone(List)

if __name__=="__main__":
    n=int(input())
    List=[]
    for i in range(n):
        List.append(int(input()))
    
    k=int(input())
    Rotate(List,k)
    for i in range(n):
        print(List[i],end=" ")
  
