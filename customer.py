from review import Review

class Customer:
    customers = [] # class variable to store all customers
    def __init__(self,given_name, family_name): 
       self._given_name = given_name
       self._family_name = family_name
       self.reviews = []
       self.customers.append(self)
    
    @property
    def given_name(self): # get the first given name
        return self._given_name
    

    @given_name.setter
    def given_name(self, new_given_name): # set the given name (new)
        self._given_name = new_given_name


    @property 
    def family_name(self): # get family name (last name)
        return self ._family_name

    


    