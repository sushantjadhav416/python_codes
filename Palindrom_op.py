def YesPalindromePossible(Str):
       ls=[]
       for i in range(len(Str)):
           if Str[i] in ls:
              ls.remove(Str[i])
           else:
               ls.append(Str[i])
        

       if len(Str)%2==0 and len(ls)==0:
             return True
       elif len(Str)%2!=0 and len(ls)==1:
             return True
       return False

if __name__=="__main__":
     Str=input()
     print(YesPalindromePossible(Str))
