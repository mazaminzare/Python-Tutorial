from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    addresses = relationship("Address", back_populates="user")

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")

Base.metadata.create_all(engine)

# Inserting data
new_user = User(name="John Doe")
session.add(new_user)
session.commit()

# Querying data
user = session.query(User).filter_by(name="John Doe").first()
print(user.name)  # Output: John Doe
