stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:")
print("AAPL = $180")
print("TSLA = $250")
print("GOOGL = $150")
print("MSFT = $420")
print("AMZN = $190")

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stocks:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stocks[stock] * quantity
    total_investment += investment

    print("Investment for", stock, "=", "$", investment)

print("\nTotal Investment = $", total_investment)