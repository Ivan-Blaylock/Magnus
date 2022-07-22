import MetaTrader5 as mt5
import numpy as np
import pandas as pd
from datetime import datetime


# This part of the program will start up the Metatrader platform
mt5.initialize()

class Meta:


    def grab_rates( symbol, num_data, timeframe, lot):
        # This method grabs all of the tick data in a way that makes it easy to implement signals
        deviation = 20

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

        # Create signals
        position = 0
        if df['Long_MA'].iloc[-1] > df['Short_MA'].iloc[-1] and position == 0:
            position += 1
            print("Short term Moving average says that we should sell!")
            request = {
                "action" : mt5.TRADE_ACTION_DEAL,
                "symbol" : symbol,
                "volume": lot,
                "type" : mt5.ORDER_TYPE_SELL,
                "price": mt5.symbol_info_tick(symbol).bid,
                "deviation": deviation,
                "type_filling": mt5.ORDER_FILLING_FOK,
                "type_time": mt5.ORDER_TIME_SPECIFIED_DAY,
            }
            mt5.order_send(request)
        elif df['Long_MA'].iloc[-1] < df['Short_MA'].iloc[-1] and position == 0:
            position += 1
            print("Short term moving average says that we should buy!")
            request = {
                "action" : mt5.TRADE_ACTION_DEAL,
                "symbol" : symbol,
                "volume": lot,
                "type" : mt5.ORDER_TYPE_BUY,
                "price": mt5.symbol_info_tick(symbol).ask,
                "deviation": deviation,
                "type_filling": mt5.ORDER_FILLING_FOK,
                "type_time": mt5.ORDER_TIME_SPECIFIED_DAY,
            }
            mt5.order_send(request)
       


        



   
    


       




    

