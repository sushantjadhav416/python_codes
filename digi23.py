def output(n,m):
    fac=1
    for i in range(1,n+1):
        fac = fac*i
    
    result = int(fac/m)

    return result

if __name__=="__main__":
    n=int(input())
    m=int(input())
    print(output(n,m))