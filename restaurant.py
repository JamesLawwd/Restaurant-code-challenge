from review import Review 
class Restaurant:
    def __init__(self,name):
        if not isinstance(name,str):
            raise Exception("Name should bea string ") # check instance and raise error if it is not a string 
        else:
            self._name = name
            self.reviews =[]


    @property
    def name(self):
        return self._name
    

    @property
    def average_star_rating(self):
        # returns the average star rating for a restaurant based on its reviews.
        # Reminder : you can caculate the average by adding up all the ratings and dividing by the number of ratings

        Average = 0
        for review in self.reviews:
            Average += review.rating
        return Average / len(self.reviews)
