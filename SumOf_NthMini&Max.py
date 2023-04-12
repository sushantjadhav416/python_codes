def output(n,List) :
  for i in range(1,n):
    Min=min(List)
    List.remove(Min)
    
  for i in range(1,n):
    Max=max(List)
    List.remove(Max)
   
  print(Min + Max)

if __name__=="__main__":
    num=int(input())
    List=[]
    n=int(input())
    for i in range(n):
        List.append(int(input()))
    output(num,List)


