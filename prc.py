n=int(input())
list=[1,2,3,4,5,6,7,8,9,10]

def mth_to_last(n):
    if n in range(len(list)):
     num=list[-n]
     return num
    else:
     return "NIL"
        

num1=mth_to_last(n)
print(num1)