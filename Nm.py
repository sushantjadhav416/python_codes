name=input("Enter the name:")
marks=int(input("Enter the marks:"))
phoneno=int(input("Enter the phone number:"))

template="""The name of the candidate:{}  his/her marks :{} phone number:{} """
output=template.format(name,marks,phoneno)
print(output)