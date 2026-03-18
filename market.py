#FIRST TASK WAS TO BUILT A DATABASE AND CALL IT NORMALLY 
# import pandas as pd

# class MarketData:

#     def __init__(self, file_path):
#         self.data = pd.read_csv(file_path)

#     def get_data(self):
#         return self.data

#     def get_close_prices(self):
#         return self.data["Close"]

#SECOND TASK WAS TO CALL THE CLOSE PRICES ONLY THE DAY YOU ARE IN RIGHT NOW

import pandas as pd

class MarketData:

    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.current_index = 0   # Start at first day

    def get_current_day(self):
        return self.data.iloc[self.current_index]

    def get_current_price(self):
        return self.data.iloc[self.current_index]["Close"]

    def next_day(self):
        if self.current_index < len(self.data) - 1:
            self.current_index += 1
            return True
        else:
            return False  # No more days

    def is_finished(self):
        return self.current_index >= len(self.data) - 1 