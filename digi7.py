txt=input()
max_cont=0
count=1

for i in range(len(txt)-1):

    if txt[i]==txt[i+1]:
        print(txt[i],txt[i+1])
        count+=1
    else:
        max_cont=max(max_cont,count)
        count=1
        max_cont=max(max_cont,count)
        if max_cont>1:
            print(max_cont)
    


