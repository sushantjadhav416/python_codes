Str=input()
Data=[]
special=[]

for i in Str:
    if i.isdigit()== False:
        Data.append(i)
for i in Data:
    if i.isalpha()== False:
        special.append(i)
for i in Data:
     if i.isalpha()== True:
        Data.append(i)


print("".join(Data) + "".join(special))