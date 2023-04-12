n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

if n%2==0:
    mid=n/2
    SW_1=l[int(mid):]
    SW_2=l[:int(mid)]
    List=SW_1+SW_2
    print(List)
else:
    mid=n/2
    SW_1=l[:int(mid)]
    SW_2=l[int(mid+1):]
    List=SW_2+[l[int(mid)]]+SW_1
    print(List)



