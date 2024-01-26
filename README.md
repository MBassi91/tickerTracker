# tickerTracker - Stock Data Fetcher

## Overview
This Python script provides a user-friendly interface to fetch historical stock data for specified tickers. Users can input a range of tickers via a CSV file, select the desired date range and data granularity, and receive consolidated stock data in a structured format.

## Features
- **CSV Input for Tickers**: Users can input multiple stock tickers through a CSV file. There's an option to skip the first row in the CSV file if it contains headers.
- **Customizable Date Range**: The script allows users to specify a start date and an optional end date for fetching historical data. If the end date is not provided, the script fetches data up to the most recent available date.
- **Selectable Data Period**: Users can select the granularity of the data (e.g., daily, weekly, monthly) through a dropdown menu.
- **Graphical User Interface**: The script features a simple yet effective GUI built with CustomTkinter, offering a more modern look and ease of use.
- **Output Customization**: Users can specify the name of the output file, which will be saved in a designated 'output/' folder.
- **Data Consolidation**: The script consolidates data from all tickers into a single CSV file, making it easy to analyze and store.

## How to Run
1. Clone or download the repository.
2. Install necessary Python libraries by running `pip install -r requirements.txt`.
3. Run the script using a Python interpreter: `python stock_data_fetcher.py`.
4. Follow the instructions in the GUI to input your data and preferences.

## How to Use
1. **CSV File Path**: Click 'Browse' to select a CSV file containing stock ticker symbols. The first column should contain the tickers.
2. **Skip First Row**: Check this box if your CSV file contains a header row.
3. **Start Date**: Enter the start date for the data fetch in YYYY-MM-DD format.
4. **End Date**: Optionally, enter the end date for the data fetch in YYYY-MM-DD format. Leave this blank to fetch data up to the current date.
5. **Period**: Select the data frequency from the dropdown menu (e.g., 1d for daily).
6. **Output File Name**: Enter a name for the output file where the data will be saved. This file will be saved in the 'output/' directory.
7. Click 'Submit' to start the data fetch process. The fetched data will be saved in the specified output file.

## Dependencies
- Python
- CustomTkinter
- Pandas
- yfinance
