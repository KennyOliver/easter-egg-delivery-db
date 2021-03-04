import csv
#====================
def scrape_csv(chosen_file,search_query):
  print(f"<-- {chosen_file}.csv -->")
  
  current_csv = open(rf"{chosen_file}.csv",'r') #open filename passed through function
  reader = csv.reader(current_csv)
  
  record_count = 0
  total_eggs = 0
  total_cost = 0
  total_shipping = 0
  
  next(reader,None) #skips header line
  for record in reader:
    brand = record[0]
    egg_type = record[1]
    size = record[2]
    price = record[3]
    shipping = record[4]
    quantity = record[5]
    
    if search_query in record:
      print(f"{brand},{egg_type},{size},£{price},£{shipping},{quantity}")
      record_count += 1
      total_eggs += int(quantity)
      total_cost += float(price)
      total_shipping += float(shipping)
  
  print("-" * 30) #UI visual divider
  print(f"Using \"{search_query}\" query...")
  stats(record_count,total_eggs,total_cost,total_shipping)
  
  current_csv.close()
#====================
def all_in_csv(chosen_file):
  print(f"<-- {chosen_file}.csv -->")
  
  current_csv = open(rf"{chosen_file}.csv",'r') #open filename passed through function
  reader = csv.reader(current_csv)
  
  record_count = 0
  total_eggs = 0
  total_cost = 0
  total_shipping = 0
  
  next(reader,None) #skips header line
  for brand,egg_type,size,price,shipping,quantity in reader:
    print(f"{brand},{egg_type},{size},£{price},£{shipping},{quantity}")
    record_count += 1
    total_eggs += int(quantity)
    total_cost += float(price)
    total_shipping += float(shipping)
  
  print("-" * 30) #UI visual divider
  print("Using \"*\" wildcard...")
  stats(record_count,total_eggs,total_cost,total_shipping)
  
  current_csv.close()
#====================
def stats(count,eggs,cost,shipping):
  print(f"{count} results")
  print(f"\tTotal eggs ordered: {eggs}")
  print(f"\tEggs cost: £{cost}")
  print(f"\tCost with shipping: £{cost + shipping}")
  avg_egg_cost = (cost) / shipping
  print(f"\tAvg cost per egg (no shipping): £{round(avg_egg_cost,3)}")
#====================
def menu():
  print("Choose the desired file to scrape:")
  for i in range(1,4+1):
    print(f"\t[{i}] order{i}.csv")
  file_choice = input("\t--> ")
  while file_choice not in ['1','2','3','4'] or len(file_choice) != 1:
    file_choice = input("\t--> ")
  
  print("Enter query\n\t[*] To print all")
  user_query = input("\t--> ")
  while len(user_query) < 1:
    user_query = input("\t--> ")
  
  print("-" * 30)
  
  if user_query != "*":
    scrape_csv(f"order{file_choice}",user_query)
  elif user_query == "*":
    all_in_csv(f"order{file_choice}")
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