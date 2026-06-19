# Expense Tracker

A Python-based expense management application that helps users record purchases, monitor spending, generate expense summaries, and manage personal financial records efficiently.

## Features

- Add multiple purchased items
- Enter prices for each item
- Store expense records in memory
- View purchased items and their prices
- Calculate total expenses
- Simple menu-driven interface
- Beginner-friendly Python project

## Technologies Used

- Python 3

## Project Structure

```bash
Expense_Tracker/
│
├── main.py
└── README.md
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/Expense_Tracker.git
```

2. Navigate to the project directory:

```bash
cd Expense_Tracker
```

3. Run the program:

```bash
python main.py
```

## Sample Output

```text
Welcome to Expense Tracker

=======Menu=======
1. Add Items that you buy
2. View your total expenses
3. Exit

Enter your choice: 1

Enter No. of items you buy
3

Enter your 1 items
Milk

Enter your 2 items
Bread

Enter your 3 items
Eggs

Enter <-Milk-> price
50

Enter <-Bread-> price
40

Enter <-Eggs-> price
80

---Expense added successfully---
```

## How It Works

- Users enter the number of purchased items.
- Item names are stored in a list.
- Prices are stored in a separate list.
- Expense data is saved using Python dictionaries.
- Total spending is calculated using Python's `sum()` function.


## Future Enhancements

- Enable automatic generation and WhatsApp delivery of expense reports to user contact number.
- Add expense categories
- Monthly expense reports
- Expense analytics and charts
- Edit and delete expenses
- Database integration
- User authentication system
- Web version using Flask
- Dashboard for expense visualization

## Author

**Aman Sharma**

Data Science Enthusiast | Building Real-World Projects

## Contribute

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

## License

This project is open-source and available for educational and learning purposes.