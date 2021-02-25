import csv
#====================
def scrape_csv(chosen_file):
  print(f"<-- {chosen_file}.csv -->")
  
  current_csv = open(rf"{chosen_file}.csv",'r') #open using filename passed through function
  reader = csv.reader(current_csv)
  
  record_count = 0 #counts number of records
  
  for record in reader:
    manufacturer = record[0]
    egg_type = record[1]
    size = record[2]
    price = record[3]
    shipping = record[4]
    quantity = record[5]
    print(f"{manufacturer},{egg_type},{size},£{price},£{shipping},{quantity}") #print each record with same appearance as a CSV file
    record_count += 1
  
  print("-" * 30) #UI visual divider
  print(f"{record_count} results found!")
  
  current_csv.close()
#====================
def menu():
  print("Choose the desired file:")
  print("\t[1] order1.csv\n\t[2] order2.csv\n\t[3] order3.csv")
  user_pick_file = input("\t--> ")
  while user_pick_file not in ['1','2','3'] or len(user_pick_file) != 1:
    user_pick_file = input("\t--> ")
  
  if user_pick_file == '1':
    scrape_csv("order1")
  elif user_pick_file == '2':
    scrape_csv("order2")
  elif user_pick_file == '3':
    scrape_csv("order3")
#====================
# MAIN PROGRAM
print("<-- Easter Egg Delivery DB -->")
print("-" * 30)
menu()

#========NOTE========
""" Use python -c 'function(argument)' to run in Bash cmd line """

""" 
Shipping Costs:
Smiths: small = 0.60 medium = 0.70 large = 0.80
Amsters: small = 0.40 medium = 0.50 large = 0.60
E&S: small = 0.90 medium = 1.00 large = 1.10
Nesters: small = 0.90 medium = 0.95 large = 0.99
"""