def getGalexy(List,n):
    for i in range(len(List)-2):
        if(List[0][i]=="#" and List[1][i]=="#" and List[2][i]=="#" ):
            print("#",end="")
        elif(List[0][i]=="#" and List[1][i]=="#" and List[2][i]=="#" ):
            p=0
        else:
            x1=i
            a=List[0][x1]
            b=List[0][x1+1]
            c=List[0][x1+2]
            a1=List[1][x1]
            b1=List[1][x1+1]
            c1=List[1][x1+2]
            a2=List[2][x1]
            b2=List[2][x1+1]
            c2=List[2][x1+2]

            if (a == '.' and b == '*' and c == '.' and a1 == '*' and b1 == '*' and c1 == '*' and a2 == '*' and b2 == '.'
                    and c2 == '*'):
 
                # If True, prA
                print("A",end="")
 
                # Increment column number
                i = i + 2
             
            # Check if the arrangement
            # of '.' and '*' forms
            # character 'E'
            if (a == '*' and b == '*' and c == '*' and a1 == '*' and b1 == '*' and c1 == '*' and a2 == '*' and b2 == '*'
                    and c2 == '*'):
 
                # If True, prE
                print("E",end="")
 
                # Increment column number
                i = i + 2
             
            # Check if the arrangement
            # of '.' and '*' forms
            # character 'I'
            if (a == '*' and b == '*' and c == '*' and a1 == '.' and b1 == '*' and c1 == '.' and a2 == '*' and b2 == '*'
                    and c2 == '*'):
 
                # If True, prI
                print("I",end="")
 
                # Increment column number
                i = i + 2
             
            # Check if the arrangement
            # of '.' and '*' forms
            # character 'O'
            if (a == '*' and b == '*' and c == '*' and a1 == '*' and b1 == '.' and c1 == '*' and a2 == '*' and b2 == '*'
                    and c2 == '*'):
 
                # If True, prO
                print("O",end="");
 
                # Increment column number
                i = i + 2
             
 
            # Check if the arrangement
            # of '.' and '*' forms
            # character 'U'
            if (a == '*' and b == '.' and c == '*' and a1 == '*' and b1 == '.' and c1 == '*' and a2 == '*' and b2 == '*'
                    and c2 == '*'):
 
                # If True, prU
                print("U",end="")
 
                # Increment column number
                i = i + 2
        
if __name__=="__main__":
    N = 18
 
    # Given matrix
    mat = [[ '*', '.', '*', '#', '*', '*', '*', '#', '*', '*', '*', '#', '*', '*', '*', '.', '*', '.'] ,
            [ '*', '.', '*', '#', '*', '.', '*', '#', '.', '*', '.', '#', '*', '*', '*', '*', '*', '*' ],
            [ '*', '*', '*', '#', '*', '*', '*', '#', '*', '*', '*', '#', '*', '*', '*', '*', '.', '*' ] ]
 
    # Function Call
    getGalexy(mat,N)