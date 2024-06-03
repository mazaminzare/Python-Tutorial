

import json
from sqlalchemy import create_engine, Column, Integer, String, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database engine
engine = create_engine('sqlite:///:memory:', echo=True)

# Define a base class for ORM models
Base = declarative_base()

# Define a simple model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create the database schema
Base.metadata.create_all(engine)

# Define an index on the 'age' column
age_index = Index('age_index', User.age)
age_index.create(bind=engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Define a function to load JSON data from a file
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Load JSON data
json_data = load_json('data.json')

# Add JSON data to the database (Create)
for entry in json_data:
    user = User(name=entry['name'], age=entry['age'])
    session.add(user)
session.commit()

# Read data from the database (Read)
print("Users aged 30 and above:")
users = session.query(User).filter(User.age >= 30).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")

# Update a user's age (Update)
user_to_update = session.query(User).filter_by(name='Alice').first()
if user_to_update:
    user_to_update.age = 28
    session.commit()
    print(f"\nUpdated Alice's age to: {user_to_update.age}")

# Read updated data from the database (Read)
print("\nUpdated Users:")
users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")

# Delete a user from the database (Delete)
user_to_delete = session.query(User).filter_by(name='David').first()
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()
    print(f"\nDeleted user: {user_to_delete.name}")

# Read final data from the database (Read)
print("\nFinal Users:")
users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")
