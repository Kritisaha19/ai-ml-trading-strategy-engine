class TradingSimulator:

    def __init__(self, initial_balance=10000):
        self.cash = initial_balance
        self.shares = 0
        self.trade_history = []

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
            print(f"Sold {quantity} shares at {price}")
        else:
            print("Not enough shares to sell.")

    def get_portfolio_value(self, current_price):
        return self.cash + (self.shares * current_price)

    def get_status(self, current_price):
        print("----- Portfolio Status -----")
        print(f"Cash: {self.cash}")
        print(f"Shares: {self.shares}")
        print(f"Current Price: {current_price}")
        print(f"Total Value: {self.get_portfolio_value(current_price)}")
        print("----------------------------\n")