List=[]
for i in "":
    List.append(i)
print(List)

List=[i for i in "sushant jadhav"]
print(List)

List=list(map(lambda x:x,"sushant jadhav"))
print(List)

List1=[i for i in range(100) if i%2==0]
print(List1)

List=[i for i in range(10)]

print(List)

List2=["even" if i%2==0 else "odd" for i in range(10)]
print(List2)

#transpose
n=int(input())
Olst=[]
List=[]
for i in range(n):
  for j in range(n):
      List.append(int(input()))
      Olst.append(List[i])

print(Olst)
   
transpose=[[row[i] for row in Olst] for i in range(n)]
print(transpose)



