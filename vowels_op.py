def output(List,ch):
   vowels=['A','E','I','O','U','a','e','i','o','u']
   for i in range(len(List)):
       for ele in vowels:
           List[i]=List[i].replace(ele,ch)
       print(List[i])
          
n=int(input())
ch=input()
List=[]
for i in range(n):
    List.append(input())
output(List,ch)

#print(List)

