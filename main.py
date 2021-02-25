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
    shipping = record[4]
    quantity = record[5]
    #print(record)
    print(f"{manufacturer},{egg_type},{size},£{price},£{shipping},{quantity}")
    line_count += 1
  print("-" * 30)
  print(f"{line_count} results found!")
  
  current_csv.close()
#====================
# MAIN PROGRAM
scrape_csv("order1")

#========NOTE========
""" Use python -c 'function(argument)' to run in Bash cmd line """

""" Smiths: small = 0.60 medium = 0.70 large = 0.80
Amsters: small = 0.40 medium = 0.50 large = 0.60
E&S: small = 0.90 medium = 1.00 large = 1.10
Nesters: small = 0.90 medium = 0.95 large = 0.99 """