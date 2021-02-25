import csv

def search(chosen_file):
  current_csv = open(f"orders/{chosen_file}.csv")
  reader = csv.reader(current_csv)
  
  for record in reader:
    print(record)