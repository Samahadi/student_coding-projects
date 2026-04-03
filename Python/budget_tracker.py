"""
Student: Sameer Ahadi
Course: CSC-101
Date: 11/16/2025
Description: Budget Tracking System
"""

import datetime
import math

monthly_budget = 0.0   
expenses = []          
income = []            


def _parse_date(date_value, field_name="date"):
    """
    Helper function to handle different date formats.

    Accepts:
        - None: returns today's date
        - datetime.date: returns as-is
        - "YYYY-MM-DD" string: converts to datetime.date

    Raises:
        TypeError or ValueError for invalid formats
    """
    if date_value is None:
        return datetime.date.today()

    if isinstance(date_value, datetime.date):
        return date_value

    if isinstance(date_value, str):
        try:
            #expected format: YYYY-MM-DD
            return datetime.date.fromisoformat(date_value)
        except ValueError as e:
            raise ValueError(f"{field_name} must be in 'YYYY-MM-DD' format") from e

    raise TypeError(f"{field_name} must be a datetime.date or 'YYYY-MM-DD' string")


def set_monthly_budget(amount, currency="USD"):
    """
    Set the monthly budget with validation.

    Args:
        amount (float or int): Must be >= 0
        currency (str): Default "USD"

    Raises:
        TypeError: If amount is not a number
        ValueError: If amount is negative

    Returns:
        str: Confirmation message with formatted amount and currency
    """
    global monthly_budget

    if not isinstance(amount, (int, float)):
        raise TypeError("amount must be a number")

    if amount < 0:
        raise ValueError("amount cannot be negative")

    monthly_budget = float(amount)
    return f"Monthly budget set to {monthly_budget:.2f} {currency}."


def add_expense(amount, category="miscellaneous", description="", date=None):
    """
    Add an expense entry.

    Args:
        amount (float or int): Must be > 0
        category (str): Converted to lowercase
        description (str): Optional
        date (datetime.date or str): If None → today. If str → must be "YYYY-MM-DD"

    Raises:
        Appropriate errors for invalid types/formats

    Returns:
        str: Confirmation message
    """
    global expenses

    #Validating amount
    if not isinstance(amount, (int, float)):
        raise TypeError("amount must be a number")
    if amount <= 0:
        raise ValueError("amount must be greater than 0")

    #Validating category
    if not isinstance(category, str):
        raise TypeError("category must be a string")
    category_lower = category.lower()

    #Validateing description
    if not isinstance(description, str):
        raise TypeError("description must be a string")

    #Handle date
    date_obj = _parse_date(date, "date")

    expense_entry = {
        "amount": float(amount),
        "category": category_lower,
        "description": description,
        "date": date_obj
    }

    expenses.append(expense_entry)

    return (
        f"Added expense: {expense_entry['amount']:.2f} "
        f"in '{expense_entry['category']}' on {expense_entry['date']}."
    )


def add_income(amount, source="salary", date=None):
    """
    Add an income entry.

    Same rules as add_expense for amount and date.
    """
    global income

    #Validate amount
    if not isinstance(amount, (int, float)):
        raise TypeError("amount must be a number")
    if amount <= 0:
        raise ValueError("amount must be greater than 0")

    #Validating source
    if not isinstance(source, str):
        raise TypeError("source must be a string")

    #Handling date
    date_obj = _parse_date(date, "date")

    income_entry = {
        "amount": float(amount),
        "source": source,
        "date": date_obj
    }

    income.append(income_entry)

    return (
        f"Added income: {income_entry['amount']:.2f} "
        f"from '{income_entry['source']}' on {income_entry['date']}."
    )


def get_remaining_budget():
    """
    Returns:
        float: monthly_budget minus sum of all expense amounts, rounded to 2 decimals
    """
    total_expenses = math.fsum(item["amount"] for item in expenses)
    remaining = monthly_budget - total_expenses
    return round(remaining, 2)


def analyze_spending(**filters):
    """
    Return spending summary based on filters.

    Valid filter keys:
        - category (str)
        - start_date (date or "YYYY-MM-DD")
        - end_date (date or "YYYY-MM-DD")
        - min_amount (float)
        - max_amount (float)

    Returns:
        dict with:
            'count': int
            'total': float (2 decimals)
            'average': float (2 decimals or 0.0 if no items)
    """
    filtered = expenses

    category = filters.get("category")
    if category is not None:
        if not isinstance(category, str):
            raise TypeError("category filter must be a string")
        cat_lower = category.lower()
        filtered = [e for e in filtered if e["category"] == cat_lower]

    #Date filters
    start_date = filters.get("start_date")
    if start_date is not None:
        start_date_obj = _parse_date(start_date, "start_date")
        filtered = [e for e in filtered if e["date"] >= start_date_obj]

    end_date = filters.get("end_date")
    if end_date is not None:
        end_date_obj = _parse_date(end_date, "end_date")
        filtered = [e for e in filtered if e["date"] <= end_date_obj]

    #Amount filters
    min_amount = filters.get("min_amount")
    if min_amount is not None:
        if not isinstance(min_amount, (int, float)):
            raise TypeError("min_amount must be a number")
        filtered = [e for e in filtered if e["amount"] >= float(min_amount)]

    max_amount = filters.get("max_amount")
    if max_amount is not None:
        if not isinstance(max_amount, (int, float)):
            raise TypeError("max_amount must be a number")
        filtered = [e for e in filtered if e["amount"] <= float(max_amount)]

    count = len(filtered)
    total = round(math.fsum(e["amount"] for e in filtered), 2)
    average = round(total / count, 2) if count > 0 else 0.0

    return {
        "count": count,
        "total": total,
        "average": average
    }


def get_spending_report(*categories):
    """
    Args:
        *categories: One or more category names (case-insensitive)

    Returns:
        dict: {category: total_spent} for requested categories
              Include categories even if total is 0.0
    """
    #If no categories requested, return empty report
    if not categories:
        return {}

    #Build totals per category from existing expenses
    totals_by_cat = {}
    for e in expenses:
        cat = e["category"]
        totals_by_cat[cat] = totals_by_cat.get(cat, 0.0) + e["amount"]

    report = {}
    for cat in categories:
        if not isinstance(cat, str):
            raise TypeError("category names must be strings")
        cat_lower = cat.lower()
        total = totals_by_cat.get(cat_lower, 0.0)
        #Keep the key as the original category name passed in
        report[cat] = round(total, 2)

    return report


# 1. Classify expense amount
# "high" (>100), "medium" (>50), otherwise "low"
categorize_expense = lambda amount: (
    "high" if amount > 100 else ("medium" if amount > 50 else "low")
)


#Helper for the days_until_payday lambda
def _days_until_payday_helper():
    """
    Assume payday is the 1st of next month.
    Return how many days from today until that date.
    """
    today = datetime.date.today()

    if today.month == 12:
        next_month = 1
        year = today.year + 1
    else:
        next_month = today.month + 1
        year = today.year

    payday = datetime.date(year, next_month, 1)
    delta = payday - today
    return delta.days


# 2. Days until next payday (assume payday is 1st of next month)
days_until_payday = lambda: _days_until_payday_helper()



if __name__ == "__main__":
    print(set_monthly_budget(2500))
    print(add_expense(75.50, "Food", "Lunch", "2025-08-10"))
    print(add_expense(150.00, "food", "Groceries"))
    print("Remaining budget:", get_remaining_budget())
    print("Food spending:", analyze_spending(category="food"))
    print("75.50 is", categorize_expense(75.50))
    print("Days until payday:", days_until_payday())
