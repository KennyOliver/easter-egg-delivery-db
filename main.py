import csv
#====================
def scrape_csv(chosen_file,search_query):
  print(f"<-- {chosen_file}.csv -->")
  
  current_csv = open(rf"{chosen_file}.csv",'r') #open using filename passed through function
  reader = csv.reader(current_csv)
  
  record_count = 0 #counts number of records
  total_eggs = 0
  total_cost = 0
  total_shipping = 0
  
  for record in reader:
    manufacturer = record[0]
    egg_type = record[1]
    size = record[2]
    price = record[3]
    shipping = record[4]
    quantity = record[5]
    
    if search_query in record:
      print(f"{manufacturer},{egg_type},{size},£{price},£{shipping},{quantity}") #print each record with same appearance as a CSV file
      record_count += 1
      total_eggs += int(quantity)
      total_cost += float(price)
      total_shipping += float(shipping)
  
  print("-" * 30) #UI visual divider
  print(f"Using \"*\" wildcard...")
  print(f"\tResults: {record_count}")
  print(f"\tTotal eggs ordered: {total_eggs}")
  print(f"\tEggs cost: £{total_cost}")
  print(f"\tCost with shipping: £{total_cost + total_shipping}")
  avg_egg_cost = (total_cost) / total_eggs
  print(f"\tAvg cost per egg (no shipping): £{round(avg_egg_cost,3)}")
  
  current_csv.close()
#====================
def all_in_csv(chosen_file):
  print(f"<-- {chosen_file}.csv -->")
  
  current_csv = open(rf"{chosen_file}.csv",'r') #open using filename passed through function
  reader = csv.reader(current_csv)
  
  record_count = 0 #counts number of records
  total_eggs = 0
  total_cost = 0
  total_shipping = 0
  
  for record in reader:
    manufacturer = record[0]
    egg_type = record[1]
    size = record[2]
    price = record[3]
    shipping = record[4]
    quantity = record[5]
    
    print(f"{manufacturer},{egg_type},{size},£{price},£{shipping},{quantity}") #print each record with same appearance as a CSV file
    record_count += 1
    total_eggs += int(quantity)
    total_cost += float(price)
    total_shipping += float(shipping)
  
  print("-" * 30) #UI visual divider
  print(f"Using \"*\" wildcard...")
  print(f"\tResults: {record_count}")
  print(f"\tTotal eggs ordered: {total_eggs}")
  print(f"\tEggs cost: £{total_cost}")
  print(f"\tCost with shipping: £{total_cost + total_shipping}")
  avg_egg_cost = (total_cost) / total_eggs
  print(f"\tAvg cost per egg (no shipping): £{round(avg_egg_cost,3)}")
  
  current_csv.close()
#====================
def menu():
  print("Choose the desired file to scrape:")
  print("\t[1] order1.csv\n\t[2] order2.csv\n\t[3] order3.csv\n\t[4] order4.csv")
  user_pick_file = input("\t--> ")
  while user_pick_file not in ['1','2','3','4'] or len(user_pick_file) != 1:
    user_pick_file = input("\t--> ")
  
  user_query = input("Enter query\n\t[*] To print all\n\t--> ")
  while len(user_query) < 1:
    user_query = input("\t--> ")
  
  print("-" * 30)
  if user_pick_file == '1':
    if user_query != '*':
      scrape_csv("order1",user_query)
    else:
      all_in_csv("order1")
  elif user_pick_file == '2':
    if user_query != '*':
      scrape_csv("order2",user_query)
    else:
      all_in_csv("order2")
  elif user_pick_file == '3':
    if user_query != '*':
      scrape_csv("order3",user_query)
    else:
      all_in_csv("order3")
  elif user_pick_file == '4':
    if user_query != '*':
      scrape_csv("order4",user_query)
    else:
      all_in_csv("order4")
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

"""
Success criteria
1. Read the data stored as records in the file.
2. Store each record in a 2D array within the program.
3. Display total Easter eggs ordered
4. Display total Easter eggs ordered from a particular manufacturer
5.The program will display total milk, plain and white chocolate eggs have been ordered.
"""