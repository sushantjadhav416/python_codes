#CPA String problem:
#1.Read a string.
#2.Read a value N. Value of N should be greater than 0 (zero).
#3.Find the N characters starting from the middle of the string.
#NOTE 1: middle=int(len(string)/2)
#NOTE 2: If the N characters are not available starting from the middle, then return up to the end of the string

#You can use/refer the below given sample input and outputs to verify your solution.
##Sample Input (below) description:
#The first line of input taken in the main section contains a String value.
#The next line of input represents the value of N, i.e. the number of characters to be extracted starting from middle of String.
##Sample Input:
#python1
#1
#Sample Output:
#h
#Sample Input:
#have123fun
#5
#Sample Output:
#123fu
#Solution:

Str=input()
num=int(input())
middle=int(len(Str)/2)
if num==1:
    print(middle)
elif len(Str)%2==0:
    middle=middle+1
    print(Str[middle:middle+num])
else:
    print(Str[middle:middle+num])
