def SOP(l):
    result=0
    for i in range(len(l)-1):
        num=l[i]
        sum,multi=0,1
        for j in range(i+1,len(l)):
            multi=num*l[j]
            sum+=multi
        result += sum
        return result

if __name__=="__main__":
    
 n=int(input())
 List=[]
 for i in range(n):
    List.append(int(input()))

 print(SOP(List))

