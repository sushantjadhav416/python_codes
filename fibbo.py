n=int(input())
sum=0
pre=0
curr=1
print(pre,end='')
print(curr,end='')
for i in range(n):
    sum=pre+curr
    pre=curr
    curr=sum


    print(sum)