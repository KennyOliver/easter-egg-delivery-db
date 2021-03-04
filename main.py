import csv
#====================
def scrape_csv(chosen_file,search_query):
  """ Print records in file that match query """
  current_csv = open(rf"{chosen_file}.csv",'r') #open filename passed through function
  reader = csv.reader(current_csv)
  
  record_count = 0
  total_eggs = 0
  total_cost = 0
  total_shipping = 0
  
  print(f"<-- {chosen_file}.csv -->")
  print("brand,type,size,price,shipping,quantity")
  next(reader,None) #skips header line
  for brand,egg_type,size,price,shipping,quantity in reader:
    if search_query in [brand,egg_type,size,price,shipping,quantity]:
      print(f"{brand},{egg_type},{size},£{price},£{shipping},{quantity}")
      record_count += 1
      total_eggs += int(quantity)
      total_cost += float(price)
      total_shipping += float(shipping)
  
  print("-" * 30)
  print(f"Using \"{search_query}\" query...")
  stats(record_count,total_eggs,total_cost,total_shipping)
  
  current_csv.close()
#====================
def all_in_csv(chosen_file):
  """ Print all records in file """
  current_csv = open(rf"{chosen_file}.csv",'r') #open filename passed through function
  reader = csv.reader(current_csv)
  
  record_count = 0
  total_eggs = 0
  total_cost = 0
  total_shipping = 0
  
  print(f"<-- {chosen_file}.csv -->")
  print("brand,type,size,price,shipping,quantity")
  next(reader,None) #skips header line
  for brand,egg_type,size,price,shipping,quantity in reader:
    print(f"{brand},{egg_type},{size},£{price},£{shipping},{quantity}")
    record_count += 1
    total_eggs += int(quantity)
    total_cost += float(price)
    total_shipping += float(shipping)
  
  print("-" * 30)
  print("Using \"*\" wildcard...")
  stats(record_count,total_eggs,total_cost,total_shipping)
  
  current_csv.close()
#====================
def stats(count,eggs,cost,shipping):
  """ Print stats for query results """
  print(f"{count} results")
  print(f"\tTotal eggs: {eggs}")
  print(f"\tTotal eggs cost: £{cost:.2f}")
  print(f"\t\t + shipping: £{(cost + shipping):.2f}")
  try:
    avg_egg_cost = (cost + shipping) / count
    print(f"\tAvg. egg (shipping): £{avg_egg_cost:.2f}")
  except ZeroDivisionError:
    print(f"\tAvg. egg (shipping): ZeroDivisionError")
#====================
def menu():
  """ User menu """
  print("Choose the desired file to scrape:")
  for i in range(1,4+1):
    print(f"\t[{i}] order{i}.csv")
  file_choice = input("\t--> ")
  while file_choice not in ['1','2','3','4'] or len(file_choice) != 1:
    file_choice = input("\t--> ")
  
  print("-" * 30) #UI visual divider
  
  print("Enter a query\n\t[*] To print all")
  user_query = input("\t--> ")
  while len(user_query) < 1:
    user_query = input("\t--> ")
  
  print("-" * 30)
  
  if user_query != "*":
    scrape_csv(f"order{file_choice}",user_query)
  elif user_query == "*":
    all_in_csv(f"order{file_choice}")
  
  print("-" * 30)
#====================
# MAIN PROGRAM
print("<-- Easter Egg Orders DB -->")
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