import yfinance as yf
from apscheduler.schedulers.blocking import BlockingScheduler
from pymongo import MongoClient
import datetime
from datetime import date

client = MongoClient('mongodb://localhost:27017/')
db = client.ICICI_Database
collection = db.CandleData

def job():
    now=datetime.datetime.now()
    ticker="ICICIBANK.NS"
    stock=yf.Ticker(ticker)
    open_price=stock.info['regularMarketOpen']
    highest_price=stock.info['regularMarketDayHigh']
    close_price=stock.info['regularMarketPreviousClose']
    volume=stock.info['regularMarketVolume']
    lowest_price=stock.info['regularMarketDayLow']
    time=now.strftime("%H:%M:%S")
    date=now.strftime("%Y-%m-%d")
    CandleStick={"Date": date, "Time": time,"Open": open_price, "Close": close_price, "Highest": highest_price, "Lowest": lowest_price, "Volume": volume}

    collection.insert_one(CandleStick)

    print(CandleStick)

scheduler=BlockingScheduler()
start_date=date.today()

for day in range(1,6):
    scheduler.add_job(job, 'interval', minutes=15, start_date =f"{start_date} 11:15:00", end_date=f"{start_date} 14:15:00")
    scheduler.start()



