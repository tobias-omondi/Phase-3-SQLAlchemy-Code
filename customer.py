from sqlalchemy import create_engine, String, Column,ForeignKey,Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class Customer(Base):
    __tablename__ = "customers"
    customerID = Column("customerId", String, primary_key=True, default=generate_uuid)
    firstName = Column("firstName", String)
    lastName = Column("lastName", String)
    email = Column("email", String)

    def __init__(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email


class Review(Base):
    __tablename__ ="reviews"
    reviewId = Column("reviewId", String,primary_key=True,default=generate_uuid)
    customerId = Column("customerId", String, ForeignKey("customers.customerId"))
    rating = Column("rating",Integer)

    def __init__(self,customerId,rating):
        self.customerId = customerId
        self.rating = rating

class Restaurant(Base):
    __tablename__ = "restaurants"
    restaurantID = Column("restaurantId", String, primary_key=True, default=generate_uuid)
    name = Column("name", String)
    price = Column("price", Integer)

    def __init__(self, name, price):
        self.name = name
        self.price = price



db = "sqlite:///ecomerceDB.db"
engine = create_engine(db)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


# Create a customer
new_customer = Customer(firstName="Mary", lastName="Agatha", email="maryagat@gmail.com")
new_customer = Customer(firstName="MORGAN", lastName="Mtua", email="morgan223@gmail.com")
new_customer = Customer(firstName="Charline", lastName="Chege", email="chege494994@gmail.com")
# new_customer = Customer(firstName="Tobias", lastName="Og", email="tobias330@gmail.com")
session.add(new_customer)
# session.add_all([])
session.commit()
print("Customer added to the database")


all_customers = session.query(Customer).all()
for customer in all_customers:
    print(f"Customer: {customer.firstName} {customer.lastName}, Email: {customer.email}")


to_query = "some_customer_id"  
customer = session.query(Customer).filter_by(customerID=to_query).first()
if customer:
    print(f"Customer: {customer.firstName} {customer.lastName}, Email: {customer.email}")
else:
    print("Customer not found")

 # Update the email
if customer:
    customer.firstName ="elsy"
    customer.email = "maryagatha@gmail.com" 
    session.commit()
    print("Customer updated")
else:
    print("Customer not found")

#Delete the customer 
if customer:
    session.delete(customer)
    session.commit()
    print("Customer deleted")
else:
    print("Customer not found")


# Create a new restaurant
new_restaurant = Restaurant(name="The OG'S Chicken Taste", price=2500)
new_restaurant = Restaurant(name="The Top Boys Burger", price=1900)
new_restaurant = Restaurant(name="The London Derby Hot Piece", price=2300)
new_restaurant = Restaurant(name= "The killer $ Hotter Pei", price=2000)

session.add(new_restaurant)
session.commit()
print("Restaurant added to the database")

# Query re...
all_restaurants = session.query(Restaurant).all()
for restaurant in all_restaurants:
    print(f"Restaurant: {restaurant.name}, Price: {restaurant.price}")

restaurant_id_to_update = "some_restaurant_id"
restaurant = session.query(Restaurant).filter_by(restaurantID=restaurant_id_to_update).first()
if restaurant:
    restaurant.name = "old kings burger"
    restaurant.price = 3000
    session.commit()
    print("Restaurant updated")
else:
    print("Restaurant not found")

# Create a new review
customer_id = "Tobias " 
rating = 3 
new_review = Review(customerId=customer_id, rating=rating)
session.add(new_review)
session.commit()
print("Review added to the database")

# Query all reviews
all_reviews = session.query(Review).all()
for review in all_reviews:
    print(f"Review ID: {review.reviewId}, Customer ID: {review.customerId}, Rating: {review.rating}")

customer_query = "Tobias"
reviews_for_customer = session.query(Review).filter_by(customerId=customer_query).all()
for review in reviews_for_customer:
    print(f"Review ID: {review.reviewId}, Customer ID: {review.customerId}, Rating: {review.rating}")


review_update = "Morgan"
review = session.query(Review).filter_by(reviewId=review_update).first()
if review:
    review.rating = 4 
    session.commit()
    print("Review updated")
else:
    print("Review not found")


review_delete = "Mary"
review_to_delete = session.query(Review).filter_by(reviewId=review_delete).first()
if review_to_delete:
    session.delete(review_delete)
    session.commit()
    print("Review deleted")
else:
    print("Review not found")


# # create customer
# firstName = "Tobias"
# lastName = "oggg"
# email ="www@gmail.com"

# customers = Customer(firstName,lastName,email)
# session.add(customers)
# session.commit()
# print("customer added to database")

# # create review
# customer_id = customers.customerID
# rating = 5 

# Review = Review(customerId=customer_id, rating=rating)
# session.add(Review)
# session.commit()
# print("Review added to the database")

# # Create restaurant
# restaurant_name = "king bugers"
# restaurant_price = 3400

# restaurant = Restaurant(name=restaurant_name, price=restaurant_price)
# session.add(restaurant)
# session.commit()
# print("Restaurant added to the database")





