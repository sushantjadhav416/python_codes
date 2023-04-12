n=int(input())
List=[int(input()) for i in range(n) ]
num=int(input())
count=0
for i in List:
    if i==num:
        count+=1

print(count)


