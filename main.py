from expense import add_expense, view_expenses, show_summary
from utils import validate_amount, validate_type, validate_category


def main():
    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Income/Expense")
        print("2. View Records")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = validate_amount(input("Enter amount: "))
            if amount is None:
                continue

            category = validate_category(input("Enter category: "))
            if category is None:
                continue

            description = input("Enter description: ")

            expense_type = validate_type(input("Type (income/expense): "))
            if expense_type is None:
                continue

            add_expense(amount, category, description, expense_type)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_summary()

        elif choice == "4":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()