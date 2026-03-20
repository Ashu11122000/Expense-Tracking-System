def validate_amount(amount: str) -> float:
    try:
        value = float(amount)
        if value <= 0:
            raise ValueError
        return value
    except ValueError:
        print("Invalid amount! Enter a positive number.")
        return None


def validate_type(expense_type: str) -> str:
    expense_type = expense_type.lower()
    if expense_type not in ["income", "expense"]:
        print("Type must be 'income' or 'expense'")
        return None
    return expense_type


def validate_category(category: str) -> str:
    if not category.strip():
        print("Category cannot be empty")
        return None
    return category