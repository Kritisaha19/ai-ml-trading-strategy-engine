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
from ml_model import PricePredictor

# Create objects
market = MarketData("data.csv")
sim = TradingSimulator()

print("Starting Trading Simulation...\n")

predictor = PricePredictor()
price_history = []

day = 0

while True:
    current_price = market.get_current_price()
    price_history.append(current_price)

    if len(price_history) > 5:
        predictor.train(price_history)

        predicted_price = predictor.predict_next(day)

        print(f"Predicted Price: {predicted_price:.2f}")

        # ✅ IMPROVED LOGIC
        if predicted_price > current_price and sim.cash >= current_price:
            print("Action: BUY")
            sim.buy(current_price, 1)

        elif predicted_price < current_price and sim.shares > 0:
            print("Action: SELL")
            sim.sell(current_price, 1)

        else:
            print("Action: HOLD")

    else:
        print("Collecting data...")

    # Show portfolio
    sim.get_status(current_price)

    day += 1

    if not market.next_day():
        break

print("\nFinal Results:")

final_price = market.get_current_price()

print("Final Portfolio Value:",
      sim.get_portfolio_value(final_price))

print("Total Profit:",
      sim.get_total_profit(final_price))

print("Total Trades:",
      sim.total_trades)
