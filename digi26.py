def output(num1,num2):
    List=[]
    for i in range(num1,num2):
        rem=i%10
        List.append(rem)
    
    
if __name__=="__main__":
    num1=int(input())
    num2=int(input())
    output(num1,num2)

    