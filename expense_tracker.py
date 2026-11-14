import csv
import os

FILE_NAME = 'expenses.csv'

def load_expenses():
    """Load previously saved expenses from the CSV file."""
    expenses = []
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row
            for row in reader:
                if row:
                    expenses.append({
                        "date": row[0], 
                        "item": row[1], 
                        "category": row[2], 
                        "amount": float(row[3])
                    })
    except FileNotFoundError:

        pass
    return expenses

def save_expense(date, item, category, amount):
    """Save a newly added expense to the CSV file."""
    file_exists = os.path.isfile(FILE_NAME)
    
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            # Write columns as requested: date,item,category,amount
            writer.writerow(["date", "item", "category", "amount"])
        writer.writerow([date, item, category, amount])

def main():
    expenses = load_expenses()
    
    while True:
        print("\n  Institute Expense Tracker ")
        print("1. Add New Expense")
        print("2. Show All Expenses")
        print("3. Calculate Total Expenses by Category")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            date = input("Enter date (DD.MM.YY): ")
            item = input("Enter item name: ")
            category = input("Enter category (e.g., Stationery, Transport): ").title()
            
            # use try catch error exeption
            while True:
                try:
                    amount = float(input("Enter amount: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid number for the amount.")
            
            save_expense(date, item, category, amount)
            expenses.append({"date": date, "item": item, "category": category, "amount": amount})
            print("Expense added successfully!")
            
        elif choice == '2':
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print("\n--- All Expenses ---")
                categories_set = set()  # Using a set to store unique categories
                
                for exp in expenses:
                    print(f"Date: {exp['date']}, Item: {exp['item']}, Category: {exp['category']}, Amount: {exp['amount']}")
                    categories_set.add(exp['category'])
                
                print("\nUnique Expense Categories:", ", ".join(categories_set))
                
        elif choice == '3':
            if not expenses:
                print("No expenses to calculate.")
            else:
                category_totals = {}
                for exp in expenses:
                    cat = exp['category']
                    category_totals[cat] = category_totals.get(cat, 0) + exp['amount']
                
                print("\n--- Total by Category ---")
                for cat, total in category_totals.items():
                    print(f"{cat}: Rs. {total}")
                    
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1 and 4.")

if __name__ == "__main__":
    main()
