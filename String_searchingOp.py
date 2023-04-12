def output(l,Nm):
    for i in l:
        if i == Nm :
            return l.index(i)
       
if __name__=="__main__":
    n=int(input())
    List=[]
    for i in range(n):
        List.append(input())
    Name=input()
    print(output(List,Name))

