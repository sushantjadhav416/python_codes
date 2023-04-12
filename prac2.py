def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 40

# check if the number of terms is valid
if nterms <= 0:
   print("0")
else:
   for i in range(nterms+1):
       print(recur_fibo(i))
