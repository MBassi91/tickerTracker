import pandas as pd
import yfinance as yf
import os


def fetch_stock_data_and_save(csv_path, start_date, end_date, period, skip_first_row, output_file):
    try:
        # Read tickers from CSV
        df = pd.read_csv(csv_path)
        if skip_first_row:
            df = df.iloc[1:]
        tickers = df.iloc[:, 0].tolist()

        # Fetch data for each ticker and store in a list
        data_frames = []
        for ticker in tickers:
            stock = yf.Ticker(ticker)
            if end_date in [None, '', ' ']:
                data = stock.history(start=start_date, interval=period)
            else:
                data = stock.history(start=start_date, end=end_date, interval=period)
            data['Ticker'] = ticker  # Add a column for the ticker symbol
            data_frames.append(data)

        # Concatenate all data frames
        combined_data = pd.concat(data_frames)

        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Save to CSV
        combined_data.to_csv(output_file)
        print(f"Data saved to {output_file}")

    except Exception as e:
        print(f"Error fetching stock data: {e}")