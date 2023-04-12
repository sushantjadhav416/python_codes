def Occurnce(Str,W):
    a=Str.split(" ")
    count=0
    for i in range(0,len(a)):
        if W==a[i]:
            count=count+1
    
    return count


if __name__ == "__main__":
    Str=input()
    word=input()
    print(Occurnce(Str,word))