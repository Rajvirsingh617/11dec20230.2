class MyParent:
    #1.1 Property (parent = baseclass)
    bloodGroup="+O"

    #1.2 Constructor


    #1.3 Method


class MyChild(MyParent):

     #1.1 Property (childclass= derived class)
    bloodGroup="+O"

    #1.2 Constructor


    #1.3 Method
    def getMyBloodGroup(self):
        print(f"My Blood Group is {self.bloodGroup}")

    # Create Class Object

co = MyChild() 
co.getMyBloodGroup()

    

     