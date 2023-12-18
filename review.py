

class Review:
    reviews = []

    def __init__(self,customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating 

    @property
    def rating(self):
        return self._rating
