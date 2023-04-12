def getIndex(listOfIntegers,NumericVariable):
        inp=int(NumericVariable)
        for i in listOfIntegers:
            if i==inp:
                b=(listOfIntegers.index(i))
                c=b+1
        
        if c<len(listOfIntegers):
            y=listOfIntegers[c:]

            for j in y:
                if j == inp:
                    d=(y.index(j))
                    res=d+c
                    
                    return res
                continue
                
        else:
            return 0     
            
if __name__ =='__main__':
        l1=[]
        size=int(input())
        for i in range(size):
            l1.append(int(input()))
        num=int(input())
        output=getIndex(l1,num)
        print(output)