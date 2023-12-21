from restaurant import Restaurant
from customer import Customer
from review import Review

# Test create_review function
def test_create_review():
    review = Review(Customer("James", "Kin"), Restaurant("Restaurant A"), 4)
    assert review.rating == 4
    assert review.customer.given_name == "James"
    assert review.restaurant.name == "Restaurant A"

# Test add_review_to_customer function
def test_add_review_to_customer():
    customer = Customer("James", "Kin")
    restaurant = Restaurant("Restaurant A")
    customer.add_review(restaurant, 5)
    assert len(customer.reviews) == 1
    assert customer.reviews[0].rating == 5

# Test average_star_rating function
def test_average_star_rating():
    restaurant = Restaurant("Restaurant A")
    customer1 = Customer("James", "Kin")
    customer2 = Customer("Sandra", "Ndeti")
    customer1.add_review(restaurant, 4)
    customer2.add_review(restaurant, 5)
    assert restaurant.average_star_rating == 4.5

# Test unique_restaurants_for_customer function
def test_unique_restaurants_for_customer():
    customer = Customer("James", "Kin")
    restaurant1 = Restaurant("Restaurant A")
    restaurant2 = Restaurant("Restaurant B")
    customer.add_review(restaurant1, 4)
    customer.add_review(restaurant2, 3)
    assert customer.restaurants == [restaurant1, restaurant2]

# Test find_customer_by_name function
def test_find_customer_by_name():
    customer1 = Customer("James", "Kin")
    found_customer = Customer.find_by_name("James Kin")
    assert found_customer == customer1

# Test find_all_customers_by_given_name function
def test_find_all_customers_by_given_name():
    customer1 = Customer("James", "Kin")
    customer2 = Customer("Sandra", "Ndeti")
    customers_with_given_name = Customer.find_all_by_given_name("James")
    assert customers_with_given_name == [customer1, customer2]

# Test num_reviews function
def test_num_reviews():
    customer = Customer("James", "Kin")
    restaurant = Restaurant("Restaurant A")
    customer.add_review(restaurant, 4)
    assert customer.num_reviews() == 1

# Run tests
test_create_review()
test_add_review_to_customer()
test_average_star_rating()
test_unique_restaurants_for_customer()
test_find_customer_by_name()
test_find_all_customers_by_given_name()
test_num_reviews()

print("All tests passed!")
