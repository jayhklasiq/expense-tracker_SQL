# Import os module to initiate the clear terminal function
import os
os.system("cls")

# Import sqlite and datetime functions
import sqlite3
from datetime import datetime

import pprint

# Connect to the database and create a cursor
connector = sqlite3.connect('database.db')
cursor = connector.cursor()

# Create the Expense table
cursor.execute('''
  CREATE TABLE IF NOT EXISTS expenses
  (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    expense_date DATE,
    category TEXT,
    amount REAL
  )
''')
connector.commit()

def add_expense(expense_date, category, amount):
    # Insert a new expense record
    cursor.execute(
        '''
        INSERT INTO expenses (expense_date, category, amount)
        VALUES (?, ?, ?)
        ''', (expense_date, category, amount)
    )
    connector.commit()

def get_all_expenses():
    # Retrieve all expenses
    cursor.execute('SELECT * FROM expenses')
    return cursor.fetchall()

def update_expense(expense_id, amount):
    # Update the amount of a specific expense
    cursor.execute(
        '''
        UPDATE expenses
        SET amount = ?
        WHERE expense_id = ?
        ''', (amount, expense_id)
    )
    connector.commit()

def delete_expense(expense_id):
    # Delete a specific expense
    cursor.execute('DELETE FROM expenses WHERE expense_id = ?', (expense_id,))
    connector.commit()

def filter_expenses_by_date(start_date, end_date):
    # Filter expenses within a date range
    cursor.execute('''
        SELECT * FROM expenses
        WHERE expense_date BETWEEN ? AND ?
    ''', (start_date, end_date))
    return cursor.fetchall()


# Test Cases for each function created
add_expense('2023-01-15', 'Groceries', 50.0)
add_expense('2023-01-20', 'Date night', 30.0)
add_expense('2023-01-15', 'Transport', 50.0)
add_expense('2023-01-20', 'Dining out', 30.0)
add_expense('2023-01-15', 'Groceries', 50.0)
add_expense('2023-01-20', 'Lunch', 30.0)

print("All Expenses:")
pprint.pprint(get_all_expenses())

update_expense(1, 60.0)

print("\nExpenses after update:")
pprint.pprint(get_all_expenses())

delete_expense(26)

print("\nExpenses after delete:")
print(get_all_expenses())

# Stretch Goal: Using Date Filtering
start_date = '2023-01-01'
end_date = '2023-01-31'
filtered_expenses = filter_expenses_by_date(start_date, end_date)

print(f"\nExpenses from {start_date} to {end_date}:")
print(filtered_expenses)

# Close the connection
connector.close()