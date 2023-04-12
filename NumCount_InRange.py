n=int(input())
List=[]
for i in range(n):
    List.append(int(input()))
start=int(input())
end=int(input())
count=0
for i in range(len(List)):
    for j in range(start,end+1):
        if List[i]==j:
            count+=1

print(count)
