from expense import add_expense, view_expenses, show_summary

def main():
    while True:
        print("\n------Expense Tracker------")
        print("1. Add Income/Expense")
        print("2. View All Records")
        print("3. Show Summary")
        print("4. Exit")
        
        choice = input("Enter your choice:")
        
        if choice == "1":
            amount = input("Enter Amount:")
            category = input("Enter Category:")
            description = input("Enter Description:")
            expense_type = input("Type (income/expense): ").lower()
            
            if expense_type not in ["income", "expense"]:
                print("Invalid Type!")
                continue
            
            add_expense(amount, category, description, expense_type)
            
        elif choice == "2":
            view_expenses()
            
        elif choice == "3":
            show_summary()
        
        elif choice == "4": 
            print("Exiting....")
            
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
