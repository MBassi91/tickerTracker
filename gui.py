import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import os

def get_user_input():
    def on_submit():
        loading_label.configure(text="Fetching data...")
        root.update_idletasks()

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
    root.grid_rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1, minsize=40)


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

    # Loading label
    loading_label = ctk.CTkLabel(root, text="")
    loading_label.grid(row=7, column=0, columnspan=3)

    user_inputs = {}
    root.mainloop()
    return user_inputs


if __name__ == '__main__':
    user_input = get_user_input()
    print(user_input)