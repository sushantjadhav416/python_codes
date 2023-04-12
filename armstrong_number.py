num=int(input())
List=[]
list1=[]
for i in range(num):
    List.append(int(input()))

sum=0
temp=List

for i in List:
 if i>0:
    rem=i%10
    sum=sum+pow(rem,3)
    i=i/10
    list1.append(sum)
    
for i in range(len(List)):
   for j in range(len(list1)):
      if List[i] == list1[j]:
          print(List[i])
      else:
          print("")
        
