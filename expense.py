from storage import load_data, save_data
from datetime import datetime
from typing import List, Dict

class Expense:
    def __init__(self, amount: float, category: str, description: str, expense_type: str):
        # Private Variable
        self._amount = amount
        self.category = category
        self.description = description
        self.type = expense_type
        self.date = datetime.now().strftime("%Y-%m-%d")
        
    def to_dict(self) -> Dict:
        return {
            "amount": self._amount,
            "category": self.category,
            "description": self.description,
            "type": self.type,
            "date": self.date
        }

def add_expense(amount, category, description, expense_type):
    data = load_data()
    
    expense = {
        "amount": float(amount),
        "category": category,
        "description": description,
        "type": expense_type
    }
    
    data.append(expense)
    save_data(data)
    
    print("Expense add successfully")
    
def view_expenses():
    data = load_data()
    
    if not data:
        print("No records found!")
        return
    
    for i, item in enumerate(data, start=1):
        print(f"{i}. {item['type']} | ${item['amount']} | {item['category']} | {item['description']}")
        
def show_summary():
    data = load_data()
        
    income = 0
    expense = 0
        
    for item in data:
        if item["type"] == "income":
            income += item["amount"]
        else:
            expense += item["amount"]
                
    print("\n Summary")
    print(f"Total income: ${income}")
    print(f"Total Expense: ${expense}")
    print(f"Balance: ${income-expense}")