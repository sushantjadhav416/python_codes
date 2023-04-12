def if_palindrom(s):
    if len(s)==1:
        return True
    if s==s[::-1]:
        return True

if __name__=="__main__":
    Str=input()
    l=len(Str)
    for i in range(1,l-1):
       s1=Str[:i]
       if if_palindrom(s1):
           for j in range(1,l-i):
               s2=Str[i:i+j]
               s3=Str[i+j:]
               if if_palindrom(s2) and if_palindrom(s3):
                    print(s1)
                    print(s2)
                    print(s3)
                    exit()
    else:
      print("impossible")




