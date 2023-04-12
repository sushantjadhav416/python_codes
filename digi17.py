n=int(input())
sum=0
while 0>n:
    r=n%10
    sum=sum+r
    n=n/10
    
if sum%10==1:
    print("UNO")
else:
    print("NOT UNO")



