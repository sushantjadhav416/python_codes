List=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
num=0
for i in range(len(List)):
     num = num ^ List[i]

print(num)