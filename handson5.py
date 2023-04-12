class students:
    def __init__(self,rollno,name,marks_list):
        self.rollno = rollno
        self.name = name
        self.marks_list = marks_list
    
    def Findgrade(self):
        Tmarks=sum(self.marks_list)
        percen=Tmarks/len(self.marks_list)
        

        if (percen < 40):
             print("F")
        if (percen >= 40 and percen < 60):
             print("C")
        if (percen >=60  and percen < 80):
             print("B")
        if (percen >= 80):
             print("A")

if __name__=="__main__":
   rollno=int(input())
   name=input()
   marks=[]
   for i in range(1,5):
       marks.append(int(input()))
   s1=students(rollno,name,marks)
   print("The grade is!!!")
   s1.Findgrade()
    

   

