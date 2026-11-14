# Institute Management Tools

## Overview
This repository contains two small Python-based management tools developed for a training institute:
1. **Institute Expense Tracker (`expense_tracker.py`):** A command-line application to record, view, and categorize daily operational expenses (like stationery, internet, transport). It saves all data persistently to a `expenses.csv` file.
2. **Student Attendance Cleaner (`attendance_cleaner.py`):** A utility script that reads raw student attendance data from `attendance.txt`, removes duplicate entries, fixes formatting issues (capitalization and spacing), and outputs a clean, alphabetically sorted list into `attendance_clean.csv`.

## Instructions to Run
1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. **To run the Expense Tracker:** Open your terminal/command prompt and run:
   ```bash
   python expense_tracker.py
   ```
4. **To run the Attendance Cleaner:** Ensure `attendance.txt` is in the same directory, then run:
   ```bash
   python attendance_cleaner.py
   ```

## Error Handling Explained
- **`FileNotFoundError`:** 
  - In `expense_tracker.py`, if `expenses.csv` does not exist when the program starts, the program catches this error and gracefully starts with an empty expense list instead of crashing.
  - In `attendance_cleaner.py`, if `attendance.txt` is missing, the program catches the error and informs the user.
- **`ValueError`:** 
  - In `expense_tracker.py`, when adding a new expense, the user is prompted to enter an amount. If they enter string text (e.g., "fifty") instead of a valid number, a `ValueError` is caught. The program then politely asks the user to enter a valid number again without stopping execution.

## Use of Sets and List Comprehensions
- **List Comprehensions:** In `attendance_cleaner.py`, a list comprehension `[name.strip().title() for name in raw_names if name.strip()]` is used to efficiently loop through all raw names, remove extra spaces using `strip()`, and format them properly using `title()` in a single line of code.
- **Sets:** 
  - In `attendance_cleaner.py`, the cleaned list of names is converted into a `set()`. Since sets do not allow duplicate values, this automatically filters out any repeated student entries.
  - In `expense_tracker.py`, a `set()` is used when displaying all expenses to extract and print only the *unique* categories (e.g., displaying "Stationery" just once, even if multiple stationery items were purchased).

## Sample Run Demonstration (Expense Tracker)

**Run 1 (Saving Data):**
```text
--- Institute Expense Tracker ---
1. Add New Expense
2. Show All Expenses
3. Calculate Total Expenses by Category
4. Exit
Enter your choice (1-4): 1
Enter date (DD-MM-YYYY): 14-11-2023
Enter item name: Whiteboard Markers
Enter category (e.g., Stationery, Transport): Stationery
Enter amount: hundred
Invalid input! Please enter a valid number for the amount.
Enter amount: 100
Expense added successfully!
```

**Run 2 (Loading Data upon restart):**
```text
--- Institute Expense Tracker ---
1. Add New Expense
2. Show All Expenses
3. Calculate Total Expenses by Category
4. Exit
Enter your choice (1-4): 2

--- All Expenses ---
Date: 14-11-2023, Item: Whiteboard Markers, Category: Stationery, Amount: 100.0

Unique Expense Categories: Stationery
```
