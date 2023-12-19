import ipdb
from review import Review
from restaurant import Restaurant
from customer import Customer

# new instances of customer
kinyanjui = Customer("kinyanjui", "James")
wangeshi = Customer("wangeshi", "winnie")
wangari = Customer("wangari", "sheenel")

Customer.all   # kinyanjui.find_by_name

restaurant1 = Restaurant("5 star")
restaurant2 = Restaurant("Everywhere")
review1 = Review(kinyanjui,restaurant1,3)

# print the number of reviews for each customer

print(review1.all_reviews)

# customer review

review2 = Review(wangeshi,restaurant2, 2)


for review in Review.all():
    print(f"Review Rating: {review.rating}, Customer Data: {review._customer.__dict__}, Restaurant Data: {review._restaurant.__dict__}")
