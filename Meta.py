
import MetaTrader5 as mt5
import numpy as np
import pandas as pd
from datetime import datetime

# This part of the program will start up the Metatrader platform
mt5.initialize()

class Meta:


    def grab_rates( symbol, num_data, timeframe):
        # This method grabs all of the tick data in a way that makes it easy to implement signals


        # First need to calculate the date of the current time
        now = datetime.now()

        # Get the rates for the financial instrument
        rates = mt5.copy_rates_from(symbol, timeframe, now, num_data)

        # Turn everything into a pandas dataframe
        df = pd.DataFrame(rates)

        # Convert the time into something that is understandable
        df['time']= pd.to_datetime(df['time'], unit='s')

        #Set the index to time
        df = df.set_index('time')

        # Create the size of the moving averages
        Short_MA = 50
        Long_MA = 200

        # Create the calculation for the moving averages in the dataframe
        df.loc[:, 'Long_MA'] = df['close'].rolling(Long_MA).mean()
        df.loc[:, 'Short_MA'] = df['close'].rolling(Short_MA).mean()

        print(df)

        return df
