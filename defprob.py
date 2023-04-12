def check(lst,check_string):
    if check_string in lst:
       return lst.index(check_string)
    else:
       return -1



n=int(input("enter legnth of the string:"))
lst=[]
for i in range(n):
    string=input(f"Enter the string{i}:")
    lst.append(string.lower())
    
check_string=input("Enetre the string you want to search:")
index_=check(lst,check_string.lower())


if index_==-1:
    print("Entered string is not in this list!!!")
else:
    print("The position od the string is:"+str(index_))

