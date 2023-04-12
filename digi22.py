def Output(num,div):
    Lrem=[]
    for i in range(num):
        rem = i % div
        Lrem.append(rem)

    print(sum(Lrem))

if __name__=="__main__":
    n=int(input())
    div=int(input())
    Output(n,div)