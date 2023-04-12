import sys
a=input().strip()
b=input().strip()
a=''.join(sorted(a)[::-1]) 
if int(a)<=int(b):
    print(-1)
    sys.exit() 
else:
    if len(a)>len(b):
        print(int(a[::-1]))
        sys.exit()
    else:
        n=len(b)
        a=list(a[::-1])
        s=''
        n1=len(a)
        for i in range(n):
            d=b[i]
            j=0
            while a[j]<b[i] and n1:
                j+=1
            if a[j]>b[i]:
                s+=a[j]
                a.remove(a[j])
                a.sort()
                s+=''.join(a)
                print(int(s)) 
                sys.exit()
            else:
                s1=s+a[j]
                g=a.copy()
                g.remove(a[j])
                if n1>1: 
                    g.sort()
                    g=g[::-1]
                    s1+=''.join(g)
                if int(s1)>int(b):
                    s+=a[j]
                    a.remove(a[j])
                    n1-=1
                else:
                    while a[j]<=b[i]:
                        j+=1
                    s+=a[j]
                    a.remove(a[j])
                    a.sort()
                    s+=''.join(a)
                    print(int(s))
                    sys.exit()
print(int(s))