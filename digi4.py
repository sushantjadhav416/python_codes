def Smallest_int(n):
    j=0
    small=[]
    if n<10:
        n=n+10

    for i in reversed(range(1,9)):
        
        while(n%i==0):
            n=n/i
            small[j]=i
            j+=1

    if n>10:
        print("Not Possible!!")

    for i in reversed(range(1,j-1)):
        print(small[i],end='')


if __name__=="__main__":
    n=int(input())
    Smallest_int(n)
