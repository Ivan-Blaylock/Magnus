from Meta import Meta
import MetaTrader5 as mt5
import time

while True:
    Meta.grab_rates(symbol="EURUSD",timeframe=mt5.TIMEFRAME_M2, num_data = 220, lot= 0.01)
    time.sleep(300)




