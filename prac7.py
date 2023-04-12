n=int(input())
array=[]
num=0
for i in range(0,n):
    array.append(int(input()))

print(array)

for i in range(0,n):
    num= num + array[i]

print(num)
