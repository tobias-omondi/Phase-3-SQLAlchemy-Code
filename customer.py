from sqlalchemy import create_engine, String, Column
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class Customer(Base):
    __tablename__ = "customers"
    customerID = Column("customerID", String, primary_key=True, default=generate_uuid)
    firstName = Column("firstName", String)
    lastName = Column("lastName", String)
    email = Column("email", String)

    def __init__(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

# Corrected the database URL to use SQLite
db = "sqlite:///ecomerceDB.db"
engine = create_engine(db)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

firstName = "Tobias"
lastName = "oggg"
email ="www@gmail.com"

customers = Customer(firstName,lastName,email)
session.add(customers)
session.commit()
print("customer added to database")