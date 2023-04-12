#Create a function count_words() which takes a string as input and creates a dictionary with a word   in the string as key and its value as number of times the word is repeating in the string. It should return the dictionary.

#eg: "hello hi hello world hello" 
          
        # dict={'hello':3,'hi':1,'word':1}

#-> Create another function max_accurance_word() which takes a string as input and returns the word which is occuring maximum number of times in the string. Use the count_words function inside this function.

#@Sample input:
#"hello hi hello world hello"

#Sample output:
#'hello'
Str=input()
def count_words(s):
  l= Str.split()
  s=set(l)
  d={}
  for i in s:
      x=l.count(i)
      d[i]=x
  return d

def max_accurance_word(Str) :
    d=count_words(Str)
    l1=[]
    for i in d.values():
        l1.append(i)
    max1=max(l1)
    for i in d.keys():
        if d[i]==max1:
          return i


print(max_accurance_word(Str))


#print(count_words(Str))
#print(s)