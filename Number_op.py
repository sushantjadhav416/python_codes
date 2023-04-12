num=int(input())
Largest_num=0
smallest_num=9
count=0

while num>0:
    rem=num%10
    count=count+rem
    if Largest_num<rem:
        Largest_num=rem
    elif smallest_num>rem:
        smallest_num=rem
    num=int(num/10)

print(Largest_num)
print(smallest_num)
print(count)