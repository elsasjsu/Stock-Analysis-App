import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from utilities import load_symbols_from_csv
from stock_data import get_stock_data

def display_stock_data(symbols):
    def fetch_and_display(event=None):
        tree.delete(*tree.get_children())
        selected_symbol = combo.get()
        data = get_stock_data(selected_symbol)
        for row in data:
            tree.insert("", tk.END, values=row)

    root = tk.Tk()
    root.title("Stock Analysis - Historical Data Viewer")

    combo = ttk.Combobox(root, values=symbols)
    combo.pack(pady=10)
    combo.bind("<<ComboboxSelected>>", fetch_and_display)

    tree = ttk.Treeview(root, columns=("Date", "Close"), show='headings')
    tree.heading("Date", text="Date")
    tree.heading("Close", text="Close Price")
    tree.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV files", "*.csv")])
    if not file_path:
        messagebox.showerror("Error", "CSV file not selected.")
    else:
        symbols = load_symbols_from_csv(file_path)
        if symbols:
            display_stock_data(symbols)
        else:
            messagebox.showinfo("No Symbols", "No stock symbols found in the CSV.")
