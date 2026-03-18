import pandas as pd
from sklearn.linear_model import LinearRegression

class PricePredictor:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, prices):
        df = pd.DataFrame(prices, columns=["price"])

        df["day"] = df.index
        X = df[["day"]]
        y = df["price"]

        self.model.fit(X, y)

    def predict_next(self, next_day):
        import pandas as pd
        return self.model.predict(pd.DataFrame([[next_day]], columns=["day"]))[0]
    