def moving_average(prices, window):
    if len(prices) < window:
        return None
    return sum(prices[-window:]) / window


def generate_signal(price_history):
    short_ma = moving_average(price_history, 3)
    long_ma = moving_average(price_history, 5)

    if short_ma is None or long_ma is None:
        return "HOLD"

    if short_ma > long_ma:
        return "BUY"
    elif short_ma < long_ma:
        return "SELL"
    else:
        return "HOLD"