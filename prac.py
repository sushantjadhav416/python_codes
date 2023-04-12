from collections import counter

def is_anagram(str1,str2):
     return counter(str1)== counter(str2)

def is_anagram(str1,str2):
     return sorted(str1)==sorted(str2)

print(is_anagram("hi","ih"))