""" This is an example of Object Oriented Programming inside a module - via Nick Delafeunte, Unit 03, DS23. """

class BareMinimumClass:
    pass

class Complex:
    def __init__(self, realpart, imagpart):
        
        """
        Constructor for Complex numbers.
        Complex numbers are part real and part imaginary. 

        """
        self.r = realpart
        self.i = imagpart

    def add(self, other_complex):
        """
        Takes another complex number and adds it to itself. 
        """
        self.r += other_complex.r
        self.i += other_complex.i


    def __repr__(self):
        return "({}, {}i)".format(self.r, self.i)





class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)
    def recieve_upvotes(self, num_upvotes=1):
        self.upvotes += num_upvotes
        
    def is_popular(self):
        return self.upvotes > 100



# class Animal:
#     """General Respresentation of Animals"""
#     def __init__(self):


#print("shown on import")
#print("not shown on import")
# if __name__ == '__main__':
    # num1 = Complex(3, -5) # num1.r == 3, and num1.i == -5
    # num2 = Complex(2, 6) # num2.r == 2 and num2.i == 6
    # num1.add(num2)
    # print(num1.r, num1.i)
    # user1 = SocialMediaUser(name="Carl", location="united states")
    # user2 = SocialMediaUser(name="Carlton", location='costa rica')
    # user3 = SocialMediaUser(name="carlos", location='argentina', upvotes=12242)
    # user4 = SocialMediaUser(name='george washington', location='djibouti', upvotes=16)

    # print('name: {}, is popular: {}, location: {}'.format(user1.name, user1.is_popular, user1.location))
    # user1.recieve_upvotes(101)
    # print('name: {}, is popular: {}, location: {}'.format(user3.name, user3.is_popular, user3.location))