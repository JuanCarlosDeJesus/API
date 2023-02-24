from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, create_engine   # create_engine creates the db and interactions
from datetime import datetime
import os


# dir of db
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = "sqlite:///" + os.path.join(BASE_DIR, 'site.db')

# the base will be the schema of the table
Base = declarative_base()

engine = create_engine(connection_string, echo=True)  # echo=True shows us the sql commands used

'''
class User:
    id int
    username str
    email str
    date_created datetime
'''
class User(Base):
    __tablename__ = "user"
    id = Column(Integer(), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.utcnow)
    
    # to view result __repr__
    def __repr__(self):
        return f"<Name {self.username}, Email {self.email}>"


new_user = User(id=1, username="Jonathan", email="Jona@than.com")
print(new_user)

