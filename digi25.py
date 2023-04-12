def calculate(a):
    b=0
    while(a > 0):
        b += a%10
        a  = a/10

    print(b)

if __name__=="__main__":
    a=int(input())
    calculate(a)
   