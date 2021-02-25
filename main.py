import csv
#====================
def search(chosen_file):
  current_csv = open(rf"{chosen_file}.csv",'r')
  reader = csv.reader(current_csv)
  
  for record in reader:
    print(record)
  
  current_csv.close()
#====================
# MAIN PROGRAM
search("order1")

#====================
""" Use python -c 'print("Hi!")' to run in Bash cmd line """