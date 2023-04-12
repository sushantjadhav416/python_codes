def check_palindrome(int_str):
  P_list=[]
  for Str in int_str:
     Str=Str.lower()
     if Str == Str[0::-1]:
           P_list.append(Str)
           for i in P_list:
              print(i)


if __name__=='__main__': 

        count=int(input()) 

        inp_str=[] 

        for i in range(count): 

                inp_str.append(input()) 
        
        check_palindrome(inp_str)
