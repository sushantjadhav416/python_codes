n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

max1=max(l)

l.remove(max1)

max2=max(l)

print(max2)
