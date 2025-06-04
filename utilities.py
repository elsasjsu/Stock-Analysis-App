import csv

def load_symbols_from_csv(file_path):
    symbols = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                symbols.append(row[0])
    return symbols
