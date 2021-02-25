import csv
#====================
def search(chosen_file):
  current_csv = open(rf"{chosen_file}.csv",'r')
  reader = csv.reader(current_csv)
  
  for record in reader:
    manufacturer = record[0]
    egg_type = record[1]
    size = record[2]
    price = record[3]
    quantity = record[4]
    #print(record)
    print(f"{manufacturer},{egg_type},{size},£{price},{quantity}")
  
  current_csv.close()
#====================
# MAIN PROGRAM
search("order1")

#========NOTE========
""" Use python -c 'function(argument)' to run in Bash cmd line """