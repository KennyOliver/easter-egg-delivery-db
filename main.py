import csv
#====================
def scrape_csv(chosen_file):
  current_csv = open(rf"{chosen_file}.csv",'r')
  reader = csv.reader(current_csv)
  
  line_count = 0
  
  for record in reader:
    manufacturer = record[0]
    egg_type = record[1]
    size = record[2]
    price = record[3]
    quantity = record[4]
    #print(record)
    print(f"{manufacturer},{egg_type},{size},£{price},{quantity}")
    line_count += 1
  print("-" * 30)
  print(f"{line_count} results found!")
  
  current_csv.close()
#====================
# MAIN PROGRAM
scrape_csv("order1")

#========NOTE========
""" Use python -c 'function(argument)' to run in Bash cmd line """