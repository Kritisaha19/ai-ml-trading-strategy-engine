class TradingSimulator:

    def __init__(self, initial_balance=10000):
        self.initial_balance = initial_balance
        self.cash = initial_balance
        self.shares = 0
        self.trade_history = []
        self.total_trades = 0

    def buy(self, price, quantity):
        total_cost = price * quantity

        if self.cash >= total_cost:
            self.cash -= total_cost
            self.shares += quantity
            self.trade_history.append({
                "type": "BUY",
                "price": price,
                "quantity": quantity
            })
            self.total_trades += 1
            print(f"Bought {quantity} shares at {price}")
        else:
            print("Not enough balance to buy.")

    def sell(self, price, quantity):
        if self.shares >= quantity:
            self.cash += price * quantity
            self.shares -= quantity
            self.trade_history.append({
                "type": "SELL",
                "price": price,
                "quantity": quantity
            })
            self.total_trades += 1
            print(f"Sold {quantity} shares at {price}")
        else:
            print("Not enough shares to sell.")

    def get_portfolio_value(self, current_price):
        return self.cash + (self.shares * current_price)

    def get_total_profit(self, current_price):
        return self.get_portfolio_value(current_price) - self.initial_balance

    def get_status(self, current_price):
        print("----- Portfolio Status -----")
        print(f"Cash: {self.cash}")
        print(f"Shares: {self.shares}")
        print(f"Current Price: {current_price}")
        print(f"Total Value: {self.get_portfolio_value(current_price)}")
        print(f"Total Profit: {self.get_total_profit(current_price)}")
        print(f"Total Trades: {self.total_trades}")
        print("----------------------------\n")
