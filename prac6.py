class player:
    def __init__(self,name,countries,age,contryf):
        self.name=name
        self.countries=countries
        self.age=age
        self.countryf=countryf

    def playercount(p_list,icountry):
      
      k=0
      for p in p_list:
       if(p.countryf.lower()==icountry.lower()):
         k+=1
      print(k)
    


def p_max_country(p_list):
  maxi=0
  o_name=''
  for p in p_list:
    if(len(p.countries)>maxi):
       maxi=len(p.countries)
       o_name=p.name
  print(o_name)

if __name__=="__main__":
 n=int(input())
 p_list =[]
 for i in range(n):
    name=input()
    kp=[]
    k=int(input())
    for j in range(k):
        kp.append(input())
    age=int(input())
    countryf=input()
    p_list.append(player(name,kp,age,countryf))
 icountry=input()
 playercount(p_list,icountry)
 p_max_country(p_list)


    



    



