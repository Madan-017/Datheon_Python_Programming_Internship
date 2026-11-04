
import csv
import math
from pathlib import Path

# --------------------------------------------------
# FILE PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATASET_FILE = BASE_DIR / "constituents.csv"
OUTPUT_FILE = BASE_DIR / "portfolio_summary.csv"

# Dictionary to store portfolio holdings
portfolio = {}


# --------------------------------------------------
# LOAD STOCK DATASET
# --------------------------------------------------

def load_stock_symbols():
    """Load stock symbols and company names from CSV."""

    stock_symbols = {}

    try:
        with open(DATASET_FILE, "r", encoding="utf-8-sig",
                  newline="") as file:

            reader = csv.DictReader(file)

            if not reader.fieldnames:
                print("Error: Dataset is empty.")
                return None

            # Normalize column headings
            columns = {
                name.strip().lower(): name
                for name in reader.fieldnames
            }

            symbol_column = columns.get("symbol")
            name_column = (
                columns.get("name")
                or columns.get("security")
            )

            if not symbol_column or not name_column:
                print("Error: Required columns not found.")
                print("Available columns:", reader.fieldnames)
                return None

            for row in reader:
                symbol = (
                    row.get(symbol_column) or ""
                ).strip().upper()

                company = (
                    row.get(name_column) or ""
                ).strip()

                if symbol and company:
                    stock_symbols[symbol] = company

        if not stock_symbols:
            print("Error: No stock symbols found.")
            return None

        return stock_symbols

    except FileNotFoundError:
        print("Error: constituents.csv not found.")
        print("Keep it in the same folder as portfolio.py.")
        return None

    except (OSError, csv.Error) as error:
        print("Error reading dataset:", error)
        return None


# --------------------------------------------------
# INPUT VALIDATION
# --------------------------------------------------

def get_positive_number(message):
    """Accept only valid positive numbers."""

    while True:
        try:
            value = float(input(message))

            if math.isfinite(value) and value > 0:
                return value

            print("Enter a number greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_positive_quantity(message):
    """Accept only positive whole numbers."""

    while True:
        try:
            quantity = int(input(message))

            if quantity > 0:
                return quantity

            print("Quantity must be greater than zero.")

        except ValueError:
            print("Enter a valid whole number.")


# --------------------------------------------------
# SAVE PORTFOLIO TO CSV
# --------------------------------------------------

def save_to_csv():
    """Save portfolio summary to an external CSV file."""

    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8",
                  newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Ticker",
                "Company",
                "Buy Price",
                "Quantity",
                "Current Price",
                "Invested Amount",
                "Current Market Value",
                "Profit/Loss",
                "Gain/Loss Percentage"
            ])

            for ticker, details in portfolio.items():

                invested = (
                    details["buy_price"] *
                    details["quantity"]
                )

                market_value = (
                    details["current_price"] *
                    details["quantity"]
                )

                profit_loss = market_value - invested

                percentage = (
                    (profit_loss / invested) * 100
                    if invested > 0 else 0
                )

                writer.writerow([
                    ticker,
                    details["company"],
                    round(details["buy_price"], 2),
                    details["quantity"],
                    round(details["current_price"], 2),
                    round(invested, 2),
                    round(market_value, 2),
                    round(profit_loss, 2),
                    round(percentage, 2)
                ])

        print("\nPortfolio CSV updated successfully!")

    except OSError as error:
        print("\nError saving CSV file:", error)


# --------------------------------------------------
# ADD STOCK TO PORTFOLIO
# --------------------------------------------------

def add_stock(stock_symbols):
    """Add a new stock or update an existing holding."""

    ticker = input("\nEnter stock ticker symbol: ").strip().upper()

    if ticker not in stock_symbols:
        print("Invalid ticker symbol.")
        print("Please select a symbol from the S&P 500 dataset.")
        return

    print("\nCompany:", stock_symbols[ticker])

    buy_price = get_positive_number(
        "Enter buying price ($): "
    )

    quantity = get_positive_quantity(
        "Enter number of shares: "
    )

    current_price = get_positive_number(
        "Enter current price ($): "
    )

    if ticker in portfolio:

        old = portfolio[ticker]

        old_quantity = old["quantity"]
        new_quantity = old_quantity + quantity

        # Calculate weighted average buying price
        total_cost = (
            old["buy_price"] * old_quantity
            + buy_price * quantity
        )

        old["buy_price"] = total_cost / new_quantity
        old["quantity"] = new_quantity
        old["current_price"] = current_price

        print("\nExisting stock holding updated.")

    else:

        portfolio[ticker] = {
            "company": stock_symbols[ticker],
            "buy_price": buy_price,
            "quantity": quantity,
            "current_price": current_price
        }

        print("\nStock added successfully!")

    # Automatically update CSV after every addition
    save_to_csv()


# --------------------------------------------------
# CALCULATE AND DISPLAY PORTFOLIO
# --------------------------------------------------

def calculate_portfolio():
    """Calculate total investment and profit or loss."""

    total_invested = 0.0
    total_market_value = 0.0

    print("\n" + "=" * 105)
    print("                 INVESTMENT PORTFOLIO SUMMARY")
    print("=" * 105)

    print(
        f"{'Ticker':<10}"
        f"{'Quantity':<10}"
        f"{'Buy Price':<14}"
        f"{'Current Price':<16}"
        f"{'Invested':<14}"
        f"{'Market Value':<16}"
        f"{'Gain/Loss %':<12}"
    )

    print("-" * 105)

    for ticker, details in portfolio.items():

        invested = (
            details["buy_price"] *
            details["quantity"]
        )

        market_value = (
            details["current_price"] *
            details["quantity"]
        )

        profit_loss = market_value - invested

        percentage = (
            (profit_loss / invested) * 100
            if invested > 0 else 0
        )

        total_invested += invested
        total_market_value += market_value

        print(
            f"{ticker:<10}"
            f"{details['quantity']:<10}"
            f"${details['buy_price']:<13.2f}"
            f"${details['current_price']:<15.2f}"
            f"${invested:<13.2f}"
            f"${market_value:<15.2f}"
            f"{percentage:>8.2f}%"
        )

    total_profit_loss = (
        total_market_value - total_invested
    )

    total_percentage = (
        (total_profit_loss / total_invested) * 100
        if total_invested > 0 else 0
    )

    print("-" * 105)

    print(f"Total Invested       : ${total_invested:.2f}")
    print(f"Total Market Value   : ${total_market_value:.2f}")
    print(f"Total Profit/Loss    : ${total_profit_loss:.2f}")
    print(f"Overall Gain/Loss    : {total_percentage:.2f}%")

    print("=" * 105)


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

def main():

    print("\n" + "=" * 55)
    print("             INVESTMENT PORTFOLIO TRACKER")
    print("=" * 55)

    stock_symbols = load_stock_symbols()

    if stock_symbols is None:
        return

    print(
        "\nSuccessfully loaded",
        len(stock_symbols),
        "stock symbols."
    )

    while True:

        print("\n--------------- MAIN MENU ---------------")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Save Portfolio to CSV")
        print("4. Exit")
        print("-----------------------------------------")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":

            add_stock(stock_symbols)

        elif choice == "2":

            if portfolio:
                calculate_portfolio()
            else:
                print("\nYour portfolio is empty.")

        elif choice == "3":

            if portfolio:
                calculate_portfolio()
                save_to_csv()
            else:
                print("\nYour portfolio is empty.")

        elif choice == "4":

            print("\nThank you for using Investment Portfolio Tracker!")
            print("Goodbye!")
            break

        else:

            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")


# --------------------------------------------------
# PROGRAM EXECUTION
# --------------------------------------------------

if __name__ == "__main__":
    main()
