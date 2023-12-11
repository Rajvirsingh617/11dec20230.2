#1. Class Defination


class Car:
    #1.1 Property = Varible
    Brand="TATA"
    Modal="2024" 

    #1.2 Constructor

    #1.3 Method/function
    def getMyBrand(self): #camleCase
        print(f"Brand is {self.Brand}")
        print(f"Modal year is {self.Modal}")

#2. create class object
# classObject = classname()
co = Car()

#Call the method with classobject
co.getMyBrand()