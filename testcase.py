import ipdb
import sqlite3
from restaurant import Restaurant
from customer import Customer
from review import Review

def test_average_star_rating():
    # Test the average star rating calculation
    restaurant1 = Restaurant("Restaurant 1")
    restaurant2 = Restaurant("Restaurant 2")

    customer1 = Customer("James", "kinyanjui")
    customer2 = Customer("Peter", "luis")

    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant1, 5)
    review3 = Review(customer1, restaurant2, 3)

    ipdb.set_trace()  # Start debugging
    assert restaurant1.average_star_rating == (4 + 5) / 2
    assert restaurant2.average_star_rating == 3

def test_customer_reviews():
    # Test the unique list of restaurants a customer has reviewed
    restaurant1 = Restaurant("Restaurant 1")
    restaurant2 = Restaurant("Restaurant 2")

    customer1 = Customer("James", "kinyanjui")
    customer2 = Customer("Peter", "luis")

    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant1, 5)
    review3 = Review(customer1, restaurant2, 3)

    ipdb.set_trace()  # Start debugging
    assert customer1.restaurants == [restaurant1, restaurant2]
    assert customer2.restaurants == [restaurant1]

def test_add_review():
    # Test adding a review to a customer
    restaurant1 = Restaurant("Restaurant 1")
    restaurant2 = Restaurant("Restaurant 2")

    customer1 = Customer("James", "kinyanjui")
    customer2 = Customer("Peter", "luis")

    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant1, 5)
    review3 = Review(customer1, restaurant2, 3)

    ipdb.set_trace()  # Start debugging
    assert customer1.num_reviews() == 2
    assert customer2.num_reviews() == 1

def test_find_by_name():
    # Test finding a customer by name
    restaurant1 = Restaurant("Restaurant 1")
    restaurant2 = Restaurant("Restaurant 2")

    customer1 = Customer("James", "kinyanjui")
    customer2 = Customer("Peter", "luis")

    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant1, 5)
    review3 = Review(customer1, restaurant2, 3)

    ipdb.set_trace()  # Start debugging
    found_customer = Customer.find_by_name("John Doe")
    assert found_customer == customer1

def test_find_all_by_given_name():
    # Test finding all customers with a given name
    restaurant1 = Restaurant("Restaurant 1")
    restaurant2 = Restaurant("Restaurant 2")

    customer1 = Customer("James", "kinyanjui")
    customer2 = Customer("Peter", "luis")

    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant1, 5)
    review3 = Review(customer1, restaurant2, 3)

    ipdb.set_trace()  # Start debugging
    found_customers = Customer.find_all_by_given_name("John")
    assert found_customers == [customer1]

def test_review_properties():
    # Test review properties
    restaurant1 = Restaurant("Restaurant 1")
    restaurant2 = Restaurant("Restaurant 2")

    customer1 = Customer("James", "kinyanjui")
    customer2 = Customer("Peter", "luis")

    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant1, 5)
    review3 = Review(customer1, restaurant2, 3)

    ipdb.set_trace()  # Start debugging
    assert review1.rating == 4
    assert review1.customer == customer1
    assert review1.restaurant == restaurant1

if __name__ == '__main__':
    test_average_star_rating()
    test_customer_reviews()
    test_add_review()
    test_find_by_name()
    test_find_all_by_given_name()
    test_review_properties()
