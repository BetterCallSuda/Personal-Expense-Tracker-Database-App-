from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# -----------------------------
# DATABASE SETUP
# -----------------------------

engine = create_engine("sqlite:///expenses.db")

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

# -----------------------------
# DATABASE MODEL
# -----------------------------

class Expense(Base):

    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    category = Column(String)
    
    description = Column(String)
    amount = Column(Float)

Base.metadata.create_all(engine)

