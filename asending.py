List=[]
print("Enter the number of elements:",)
num=int(input())
for i in range(num):
    List.append(int(input()))

for i in range(0,num):
    for j in range(0,num):
        if(List[i]<List[j]):
            temp=List[i]
            List[i]=List[j]
            List[j]=temp

print("!!!The list  in asending order!!!")
#for i in range(0,num):
print(List)