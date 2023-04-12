def IsBracketbalaced(inp):
    stack=[]
    for char in inp:
        if char in ["(","[","{"]:
            stack.append(char)
        else:
           if  not stack:
               return False
           current_char=stack.pop()
           if current_char == "(":
               if char ==')':
                   return False
           if current_char == "[":
               if char ==']':
                   return False
           if current_char =="{":
               if char =='}':
                   return False
    
    if stack:
        return False
    else:
        return True



if __name__=="__main__":
 inp=input()

 if IsBracketbalaced:
    print("True")
 else:
    print("false")

