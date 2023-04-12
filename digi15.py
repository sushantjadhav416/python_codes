#count no of characters in string
Str=input()
freq=[Str.count(i) for i in Str]
print(freq)
print(max(freq))