def check_prime(n): 
 temp=False 
 for i in range(2,n): 
   if n%i==0: 
      temp=True 
   if temp==False:
      return 1 
   else:
      return 0 

def prime_composite_list(inp):
    List=[]
    cmlist=[]
    prime=[]
    for i in inp:
       if check_prime(i)==1:
           prime.append(i)
       else:
           cmlist.append(i)
    List.append(prime)
    List.append(cmlist)
    return List
    
if __name__=='__main__':
 inp=[]
 count=int(input())
 for i in range(count):
    inp.append(int(input()))

 print(check_prime(inp[1]))
 result=prime_composite_list(inp)
 print(result)