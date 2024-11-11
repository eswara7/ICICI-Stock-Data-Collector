# ICICI Stock Data Collector

## Overview

This project is designed to collect real-time stock market data for **ICICI Bank** using the **Yahoo Finance API (`yfinance`)** and store it in a **MongoDB** database. The tool automatically fetches stock data every 15 minutes on weekdays using **APScheduler**, providing crucial information such as the opening price, highest price, closing price, lowest price, and trading volume. This project can be expanded for further analysis, such as stock price prediction, visualization, and trend analysis.

 Stock Market Data Collection & Analysis Tool

## Features

- **Real-Time Data Collection**: Fetches real-time stock data every 15 minutes.
- **MongoDB Database Integration**: Stores the collected data in a **MongoDB** database for easy access and analysis.
- **Automated Scheduling**: Uses **APScheduler** to schedule the data collection at regular intervals on weekdays.
- **Data Metrics Collected**:
  - Open Price
  - Highest Price of the Day
  - Closing Price
  - Lowest Price of the Day
  - Volume of Trades
  - Timestamp (Date and Time)

## Tools & Technologies Used

- **Python**: Primary programming language used to develop the tool.
- **yfinance**: Yahoo Finance API used for fetching real-time stock data.
- **MongoDB**: NoSQL database used for storing stock data.
- **APScheduler**: Scheduling library used to automate data collection at regular intervals.
- **Datetime**: Standard Python library used to handle time and date-related tasks.