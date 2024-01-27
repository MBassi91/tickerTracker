# Stock Data Fetcher

## Overview
This Python script provides a user-friendly interface to fetch historical stock data for specified tickers. Users can input a range of tickers via a CSV file, select the desired date range and data granularity, and receive consolidated stock data in a structured format.

## Structure
- `gui.py`: Contains the code for the graphical user interface.
- `data_processing.py`: Handles fetching and saving the stock data.
- `tickerTracker.py`: The main script that orchestrates the flow of the application.

## Features
- **CSV Input for Tickers**: Input multiple stock tickers through a CSV file with an option to skip the first row.
- **Customizable Date Range**: Specify start and optional end dates for fetching historical data.
- **Selectable Data Period**: Choose data frequency (e.g., daily, weekly, monthly) via a dropdown menu.
- **Graphical User Interface**: A modern GUI built with CustomTkinter.
- **Output Customization**: Specify the output file name, saved in the 'output/' directory.
- **Data Consolidation**: Consolidate data from all tickers into a single CSV file.

## How to Run
1. Clone or download the repository.
2. Install necessary Python libraries by running `pip install -r requirements.txt`.
3. Run the main script: `python tickerTracker.py`.
4. Follow the instructions in the GUI to input your data and preferences.

## How to Use
1. **CSV File Path**: Use 'Browse' to select a CSV file with stock tickers.
2. **Skip First Row**: Check if your CSV has a header row.
3. **Start Date**: Enter the start date (YYYY-MM-DD).
4. **End Date**: Optionally, enter the end date (YYYY-MM-DD).
5. **Period**: Select data frequency from the dropdown (e.g., '1d').
6. **Output File Name**: Enter a name for the output file.
7. Click 'Submit' to fetch data and save it to the specified output file.

## Dependencies
- Python
- CustomTkinter
- Pandas
- yfinance
