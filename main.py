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


# -----------------------------
# ADD EXPENSE
# -----------------------------

def add_expense():

    category = input("Category (food/travel/shopping/etc): ")
    description = input("Description: ")
    amount = float(input("Amount: "))

    expense = Expense(
        category=category,
        description=description,
        amount=amount
    )

    session.add(expense)
    session.commit()

    print("✅ Expense added successfully")


