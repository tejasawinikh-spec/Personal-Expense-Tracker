# Personal Expense Tracker with CSV

## Project Overview

The Personal Expense Tracker is a beginner-friendly Python application designed to help users record and manage their daily expenses.

Users can add expenses, view all transactions, filter expenses by category or month, and generate spending summaries.

All expense records are stored in a CSV file, ensuring that data remains saved even after closing and restarting the application.

## Features

- Add new expenses with date, category, description, and amount.
- View all recorded expenses.
- Filter expenses by category.
- Filter expenses by month.
- Calculate total spending for each category.
- Display the grand total of all expenses.
- Identify the biggest single expense.
- Store expense records permanently using CSV files.
- Validate dates and amounts.
- Simple menu-driven interface.

## Technologies Used

- Python 3
- CSV Module
- Datetime Module
- Visual Studio Code

## Project Structure

```text
PersonalExpenseTracker/
│
├── expense_tracker.py
├── expenses.csv
└── README.md
```

## Requirements

- Python 3.10 or newer.
- Visual Studio Code or any Python-supported editor.

No external libraries are required.

## How to Run

**Step 1: Clone the repository**

```bash
git clone https://github.com/tejasawinikh-spec/Personal-Expense-Tracker.git
```

**Step 2: Open the project folder**

```bash
cd PersonalExpenseTracker
```

**Step 3: Run the application**

```bash
python expense_tracker.py
```

## Application Menu

```text
===================================
       PERSONAL EXPENSE TRACKER
===================================
1. Add Expense
2. View All Expenses
3. Filter Expenses
4. Expense Summary
5. Quit
===================================
```

## CSV File Format

Expenses are stored in `expenses.csv` with four columns:

| Date | Category | Description | Amount |
|---|---|---|---:|
| 2026-11-20 | Food | Lunch | 120.00 |
| 2026-11-20 | Study | Python | 200.00 |
| 2026-11-20 | Bills | Electricity | 2000.00 |
| 2026-10-26 | Fun | Party | 5000.00 |

The application automatically creates the CSV file with the required headers if it does not exist.

## Concepts Learned

- Python functions and loops.
- Conditional statements.
- File handling.
- CSV reading and writing.
- Date and amount validation.
- Exception handling.
- Lists and dictionaries.
- Filtering and grouping data.
- Calculating totals and maximum values.

## Problem Faced and Solution

**Problem:** Initially, individual functions had to be executed separately to test different features.

**Solution:** Implemented a menu-driven system using a while loop and conditional statements. This allows users to access all application features through a single interface.

## Future Improvements

- Add expense editing and deletion.
- Generate monthly spending reports.
- Display expense charts and graphs.
- Develop a graphical user interface.

## Author

**Tejaswini Krishna Hulswar**

**Project:** Personal Expense Tracker with CSV

**Programming Language:** Python

**InternCircle – Python Programming Project 03**
