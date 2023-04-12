def output(s):
    Na=["@","#",".","(",")","*",]
    for i in s:
        if i in Na:
          return False
    return True 

if __name__=="__main__":
    Str=input()
    print(output(Str))