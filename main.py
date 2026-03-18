# from market import MarketData

# market = MarketData("data.csv")

# data = market.get_data()

# print("Full Data:")
# print(data)

# print("\nClose Prices:")
# print(market.get_close_prices())

# --------------------------------------------
# from market import MarketData

# market = MarketData("data.csv")

# print("Starting Market Simulation...\n")

# while True:
#     day_data = market.get_current_day()
#     print(f"Date: {day_data['Date']} | Close Price: {day_data['Close']}")

#     if not market.next_day():
#         break

# print("\nSimulation Finished.")

# --------------------------------------------
from strategy import generate_signal
from market import MarketData
from trading import TradingSimulator

# Create objects
market = MarketData("data.csv")
sim = TradingSimulator()   # ⚠️ THIS LINE WAS MISSING OR WRONG

print("Starting Trading Simulation...\n")
price_history = []
while True:
    current_price = market.get_current_price()
    price_history.append(current_price)

    signal = generate_signal(price_history)

    if signal == "BUY":
        sim.buy(current_price, 1)
    elif signal == "SELL":
        sim.sell(current_price, 1)

    print("Signal:", signal)
    sim.get_status(current_price)

    if not market.next_day():
        break

print("\nFinal Results:")

print("Final Portfolio Value:",
      sim.get_portfolio_value(market.get_current_price()))

print("Total Profit:",
      sim.get_total_profit(market.get_current_price()))

print("Total Trades:",
      sim.total_trades)