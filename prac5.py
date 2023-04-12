class books:
    def __init__(self,book_id ,Book_name):
        self.bookId=book_id
        self.BookNm=Book_name

class library:
    def __init__(self,book_id,address,Book_lst):
        self.book_id=book_id 
        self.address=address
        self.Book_lst=book_lst
    def count_books(self,ch):
        count=0
        for i in self.book_lst:
            if i.booknm[0]==ch:
                count+=1
        return count
    def delet_books(self,list1):
        for i in list1:
            for b in self.Book_list:
                if b.booknm==i:
                    self.Book_list.remove(b)


if __name__=="__main__":
  n=int(input())
  book_lst=[]
  for i in range(n):
    bookid=int(input())
    booknm=input()
    book_lst.append(books(bookid,booknm))
  ch=input()
  D=library("233","mumbai",book_lst)
  d_n=int(input())
  list1=[]
  for i in range(d_n):
    name=input()
    list1.append(name)
  print(D.count_books(ch))
  D.delet_books(Book_list)

  for i in D.book_lst:
        print(i.booknm)



    
    
