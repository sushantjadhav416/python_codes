class Associate:
    def __init__(self,id,name,technology,ExpInYr):
        self.id=id
        self.name=name
        self.technology=technology
        self.ExpInYr=ExpInYr
    
class solution:
    @classmethod
    def AssociatesForGivenTechnology(cls,Asso_List,req_tech):
        req_list=[]
        for i in Asso_List:
            if i.technology == req_tech and i.ExpInYr % 5 == 0:
                req_list.append(i.id)
        return req_list



if __name__=="__main__":
    n=int(input())
    Asso_List=[]
    for i in range(n):
        id=int(input())
        name=input()
        tech=input()
        exp=int(input())
        Asso_List.append(Associate(id,name,tech,exp))
    
    req_tech=input()

    output=solution.AssociatesForGivenTechnology(Asso_List,req_tech)
    for i in output:
        print(i)
    


