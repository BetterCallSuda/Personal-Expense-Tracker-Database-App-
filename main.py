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


# -----------------------------
# VIEW EXPENSES
# -----------------------------

def view_expenses():

    expenses = session.query(Expense).all()

    print("\n📊 All Expenses\n")

    for e in expenses:
        print(f"{e.id} | {e.category} | {e.description} | ₹{e.amount}")

    print()


# -----------------------------
# TOTAL SPENDING
# -----------------------------

def total_spending():

    expenses = session.query(Expense).all()

    total = sum(e.amount for e in expenses)

    print(f"\n💰 Total Spending: ₹{total}\n")


# -----------------------------
# CATEGORY REPORT
# -----------------------------

def category_report():

    category = input("Enter category: ")

    expenses = session.query(Expense).filter_by(category=category).all()

    total = sum(e.amount for e in expenses)

    print(f"\nTotal spent on {category}: ₹{total}\n")


# -----------------------------
# DELETE EXPENSE
# -----------------------------

def delete_expense():

    expense_id = int(input("Enter expense ID to delete: "))

    expense = session.query(Expense).filter_by(id=expense_id).first()

    if expense:

        session.delete(expense)
        session.commit()

        print("🗑 Expense deleted")

    else:

        print("Expense not found")


# -----------------------------
# MAIN MENU
# -----------------------------

def main():

    while True:

        print("==== EXPENSE TRACKER ====")
        print("1 Add Expense")
        print("2 View Expenses")
        print("3 Total Spending")
        print("4 Category Report")
        print("5 Delete Expense")
        print("6 Exit")

        choice = input("Select option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_spending()

        elif choice == "4":
            category_report()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            print("Goodbye")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
