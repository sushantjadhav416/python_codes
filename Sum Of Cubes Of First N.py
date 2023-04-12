def sumofcubes(N):
    cubsum=1

    for i in (2,N+1):
       cubsum += i**3

    return cubsum

if __name__=="__main__":
  num=int(input())
  print(sumofcubes(num))