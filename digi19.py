def output(n):
    c=0
    if n!=1:
        while n!=1:
            for i in range(n-1,0,-1):
                if(n%i==0):
                    n=n-i
                    c=c+1
                    break
    return c+1


if __name__=="__main__":
  num=int(input())
  print(output(num))