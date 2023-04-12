def output(Strings,Str):
    count=0
    for i in range(len(Strings)):
        if Str.lower() == Strings[i].lower():
            count=count+1
    print(count)

if __name__=="__main__":
    n=int(input())
    Strings=[]
    for i in range(n):
       Strings.append(input())
    
    Str=input()
    output(Strings,Str)
    

