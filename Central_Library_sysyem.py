#Name:sushant vikas jadhav
#Central library system // 
class library:
    def __init__(self,listbooks):
        self.books=listbooks
    def displayavailable(self):
        print("!!!!!The available books are!!!!")
        for book in self.books:
            print('*'+book)

    def borrowdbook(self,bookname):
        if bookname in self.books:
            print(f"\n****You issued this {bookname}.please Keep it safe and return it in 30 days!!*****")
            self.books.remove(bookname)
        else:
            print("!!!Soory!! This book is not present in the library or this book has already been issued!!!!")

    def returnbook(self,bookname):
        self.books.append(bookname)
        print("Thanks for returning this book!! have nice day!!")

class students:
    def requastbook(self):
        self.book=input("Enter the book name you want enter:")
        return self.book
    def returnbook(self):
        self.book=input("Enter the book name you want enter:")
        return self.book
        
        
if __name__== "__main__":
    centralLibrary=library(["c programming","python notes","oops concets"])
    Student=students()
    #centralLibrary.displayavailable()
    while(True):
        Welcome='''*****Welcome to the centeral library system*****
        chose options : press
        1) Listing all the books
        2) Request a book
        3) Add or Return a book
        4) Exit a library 
        '''
        print(Welcome)
        choice=input("Enter your choice:")
        if choice=='1':
           centralLibrary.displayavailable()
           print("\n")
        elif choice=='2':
           centralLibrary.borrowdbook(Student.requastbook())
           print("\n")
        elif choice=='3':
            centralLibrary.returnbook(Student.returnbook())
            print("\n")
        elif choice=='4':
            print("Thanks for using this library!!!")
            exit()
        else:
            print("Invalid entry!!")
        
