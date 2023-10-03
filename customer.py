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

class review(Base):
    reviewId = Column("reviewId", String,primary_key=True,default=generate_uuid)
    customerId= Column("customerId", String, ForeignKey("customerId"))
    rating = Column("rating",Integer)

    def __init__(self,customerid,reviewid,rating):
        self.customerid = customerid
        self.reviewid = reviewid
        self.rating = rating


db = "sqlite:///ecomerceDB.db"
engine = create_engine(db)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# create customer
firstName = "Tobias"
lastName = "oggg"
email ="www@gmail.com"

customers = Customer(firstName,lastName,email)
session.add(customers)
session.commit()
print("customer added to database")

# create review