class DairyProduct :
 
    # Define a constructor method
    # for initializing its attributes
    def __init__(self, *args) :
 
        # * is generally used for taking
        # variable number of arguments
        # in function/method
         
        # args is tuple of arguments
        # so we can access these arguments
        # with indices
        self.dairyId = int(args[0])
        self.dairyBrand = args[1]
        self.productType = args[2]
        self.price = int(args[3])
        self.grade = args[4]
 
# Create a ProductGrade 
# class with its attributes
# and method
class ProductGrade :
 
    # Define a constructor method
    # for initializing its attributes
    def __init__(self, *args) :
 
        self.dairyList = args[0]
        self.weightageDict = args[1]
 
    # Define a method for updating the price
    # as per requirement and return list of
    # tuple of brand name and its updated price
    def priceBasedOnBrandAndType(self, brand, ptype) :
 
        # empty list
        ans = []
 
        # iterate through each DairyProduct
        # objects present in the list
        for obj in self.dairyList :
 
            # if given condition is satisfied then
            # update the price for that brand
            # and appending into the list 
            if obj.dairyBrand == brand and obj.productType == ptype :
 
                obj.price += (obj.price * self.weightageDict[obj.grade]) / 100
 
                ans.append((brand, obj.price))
 
        # if list is empty then return
        # None otherwise return
        # that list
        if len(ans) :
            return ans
        else :
            return None
 
# Main program starts here
if __name__ == "__main__" :
 
    # read the number of DairyProduct 
    n1 = int(input())
 
    # empty list
    dairyProducts = []
 
    # Create a n1 number of
    # DairyProduct objects
    for i in range(n1) :
 
        # reading the data related
        # to DairyProduct class
        dId = input()
        dBrand = input()
        pType = input()
        price = input()
        grade = input().lower()
 
        # Create DairyProduct object 
        # with its attributes
        dpObj = DairyProduct(dId, dBrand, pType, price, grade)
 
        # adding DairyProduct object
        # to the list
        dairyProducts.append(dpObj)
 
    #  read the number of dictionary elements
    n2 = int(input())
 
    # empty dictionary
    weightageDict = {}
 
     
    for i in range(n2) :
 
        # reading the key,value
        # pair for a dictionary
        grade = input().lower()
        value = int(input()) 
 
        # insert key,value pair
        # to the dictionary
        weightageDict[grade] = value
 
    # Create ProductGrade object 
    # with its attributes
    pgObj = ProductGrade(dairyProducts, weightageDict)
 
    # reading brand name and product type
    dairyBrand = input()
    producttype = input()
 
    # priceBasedOnBrandAndType() method called
    rslt = pgObj.priceBasedOnBrandAndType(dairyBrand, producttype)
 
    # if rslt is not empty
    # then print required outputs
    # otherwise print message
    # "No dairy product found"
    if rslt :
         
        for item in rslt :
            print("Dairy Brand:", item[0])
            print("Price:", item[1])
             
    else :
        print("No dairy product found")