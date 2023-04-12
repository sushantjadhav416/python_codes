Str1=input()
Str2=input()

if "".join(sorted(Str1)) == "".join(sorted(Str2)):
    print("This  is an anagram!!!")
else:
    print("This is not an anagram!!!")
