# Investment Portfolio Tracker – Python Programming Internship

## 1. Project Overview

The Investment Portfolio Tracker is a Python-based application that helps users manage and monitor their stock investments.

Users can enter stock ticker symbols, buying prices, share quantities, and current stock prices. The application calculates the total invested amount, current market value, and profit or loss for each stock.

It also generates a CSV report containing the portfolio details and calculated results.

## 2. Features

- Loads stock ticker symbols and company names from an S&P 500 CSV dataset.
- Allows users to add stock holdings.
- Accepts buying price, current price, and share quantity.
- Stores portfolio information using a Python dictionary.
- Calculates total invested capital.
- Calculates current market value.
- Calculates individual stock profit or loss.
- Calculates percentage gain or loss.
- Displays portfolio details in a formatted console table.
- Automatically generates and updates a CSV summary.
- Validates user inputs and handles invalid ticker symbols.

## 3. Technologies Used

- Python 3
- CSV module
- Math module
- Pathlib module
- File handling
- Dictionary data structure

## 4. Project Structure

```text
Task-2-Portfolio-Tracker/
│
├── portfolio.py
├── constituents.csv
├── portfolio_summary.csv
└── README.md
```

## 5. How to Run the Project

1. Install Python 3.
2. Download or clone the project repository.
3. Keep `portfolio.py` and `constituents.csv` in the same folder.
4. Open the project folder in Visual Studio Code.
5. Open the terminal.
6. Execute the following command:

```bash
python portfolio.py
```

## 6. How to Use

The application provides four menu options:

1. Add Stock – Enter the ticker symbol, buying price, quantity, and current price.
2. View Portfolio – Display all holdings and their investment performance.
3. Save Portfolio to CSV – Generate or update the portfolio summary file.
4. Exit – Close the application.

## 7. Calculation Methods

**Invested Amount**

Buy Price × Quantity

**Current Market Value**

Current Price × Quantity

**Profit or Loss**

Current Market Value − Invested Amount

**Gain or Loss Percentage**

(Profit or Loss ÷ Invested Amount) × 100

## 8. Output

The application displays a formatted portfolio summary containing:

- Stock ticker and quantity
- Buying price and current price
- Invested amount
- Current market value
- Individual gain or loss percentage
- Overall portfolio profit or loss

The results are also stored in `portfolio_summary.csv`.

## 9. Limitations

- Current stock prices are entered manually by the user.
- The S&P 500 dataset provides ticker symbols and company names, not live market prices.
- The portfolio data is stored during the program session; it is not automatically restored from a previous session.

## 10. Conclusion

The Investment Portfolio Tracker provides a simple way to manage stock holdings and calculate investment performance.

This project demonstrates Python programming concepts such as dictionaries, functions, loops, conditional statements, CSV handling, file operations, and input validation.

## Internship Details

**Datheon – Python Programming Internship**

**Task 2: Investment Portfolio Tracker**