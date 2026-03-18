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

from market import MarketData
from trading import TradingSimulator

market = MarketData("data.csv")
sim = TradingSimulator()

print("Starting Trading Simulation...\n")

while True:
    current_price = market.get_current_price()

    # Simple dummy strategy:
    if current_price < 110:
        sim.buy(current_price, 1)
    elif current_price > 115:
        sim.sell(current_price, 1)

    sim.get_status(current_price)

    if not market.next_day():
        break

print("Simulation Finished.\n")

print("Final Portfolio Value:",
      sim.get_portfolio_value(market.get_current_price()))