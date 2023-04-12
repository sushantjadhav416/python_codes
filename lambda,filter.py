#l=[23,45,2,3,3,4,56,56,6,7,55,80,20]
#a=filter(lambda a: a%5==0,l)
#print(list(a))
l=[23,45,2,3,3,4,56,56,6,7,55,80,20]
even=filter(lambda even:even%2==0,l)
odd=filter(lambda even:even%2!=0,l)
print("List of even numbers:",list(even))
print("List of odd numbers:",list(odd))

