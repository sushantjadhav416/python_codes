def word_count(List,fstr):
    cnt=0
    for i in List:
        if(fstr.lower() in i.lower()):
            cnt+=1
    return cnt

if __name__ == "__main__":
    n=int(input())
    List=[]
    for i in range(n):
        Str=input()
        List.append(Str)
    
    Fstr=input()
    
    print(word_count(List,Fstr))


