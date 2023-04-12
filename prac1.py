import math
c=50
h=30
ListNum=[]
n=int(input())
for i in range(n):
    ListNum.append(int(input()))

value=[]
for d in ListNum:
    value.append(round(math.sqrt(2*c*d/h)))

print(",".join(value))


#for i in  value:
#    print(i,end=",")

 


