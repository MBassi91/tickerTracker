import os
import pandas as pd
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import yfinance as yf

import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


def get_user_input():
    def on_submit():
        user_inputs['start_date'] = start_date_entry.get()
        user_inputs['end_date'] = end_date_entry.get()
        user_inputs['period'] = period_combobox.get()
        user_inputs['csv_path'] = csv_path_entry.get()
        user_inputs['output_file'] = os.path.join('output', output_file_entry.get())
        user_inputs['skip_first_row'] = skip_var.get()
        root.quit()

    def browse_file():
        filename = filedialog.askopenfilename(filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        csv_path_entry.delete(0, tk.END)
        csv_path_entry.insert(0, filename)

    root = ctk.CTk()
    root.title("Stock Data Fetcher")
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1, minsize=40)

    ctk.CTkLabel(root, text="CSV File Path:").grid(row=0, column=0, sticky="w")
    csv_path_entry = ctk.CTkEntry(root)
    csv_path_entry.grid(row=0, column=1, sticky="ew")
    browse_button = ctk.CTkButton(root, text="Browse", command=browse_file)
    browse_button.grid(row=0, column=2, padx=10)

    ctk.CTkLabel(root, text="Skip First Row:").grid(row=1, column=0, sticky="w")
    skip_var = tk.BooleanVar()
    skip_check = ctk.CTkCheckBox(root, text=None, variable=skip_var)
    skip_check.grid(row=1, column=1, sticky="w")

    ctk.CTkLabel(root, text="Start Date (YYYY-MM-DD):").grid(row=2, column=0, sticky="w")
    start_date_entry = ctk.CTkEntry(root)
    start_date_entry.grid(row=2, column=1, sticky="ew")

    ctk.CTkLabel(root, text="End Date (YYYY-MM-DD):").grid(row=3, column=0, sticky="w")
    end_date_entry = ctk.CTkEntry(root)
    end_date_entry.grid(row=3, column=1, sticky="ew")

    ctk.CTkLabel(root, text="Period:").grid(row=4, column=0, sticky="w")
    period_combobox = ctk.CTkComboBox(root, values=('1d', '1wk', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'))
    period_combobox.grid(row=4, column=1, sticky="ew")
    period_combobox.set("1d")

    ctk.CTkLabel(root, text="Output File Name:").grid(row=5, column=0, sticky="w")
    output_file_entry = ctk.CTkEntry(root)
    output_file_entry.grid(row=5, column=1, sticky="ew")
    output_file_entry.insert(0, "stock_data.csv")

    submit_button = ctk.CTkButton(root, text="Submit", command=on_submit)
    submit_button.grid(row=6, column=0, columnspan=3)

    user_inputs = {}
    root.mainloop()
    return user_inputs




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


if __name__ == '__main__':
    user_inputs = get_user_input()
    fetch_stock_data_and_save(user_inputs['csv_path'], user_inputs['start_date'], 
                              user_inputs['end_date'], user_inputs['period'], 
                              user_inputs['skip_first_row'], user_inputs['output_file'])