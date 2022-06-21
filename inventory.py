# This program reads inventory.txt file and captures new items and add them
# on the file
# Import tabulate libray
from tabulate import tabulate

class Shoe():
    # Initialize object list
    shoe_list = []
    # Constructor allows us to set the counrty, code, produc, cost
    # and quantity as instance variables
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        # Adds the instance variables to list
        Shoe.shoe_list.append([self.country,self.code,self.product,self.cost,\
                               self.quantity])
         
    def read_data():
        # This function reads the data from inventory text file and creates
        # creates shoe opjects 
        try:
            with open("inventory.txt", "r") as f:
                for line in f:
                    product_details = line.split(",")
                    shoe_object = Shoe(product_details[0],product_details[1],\
                                       product_details[2],product_details[3],\
                                       product_details[4].strip())
        except FileNotFoundError:
            print("Sorry 'inventory.txt' file was not found")
 
    def search_product(product_code):
        # This function searches the product from object list by code
        # and returns True if the product was found
        found = False
        # Initialize object list 
        temp_list = []
        # Header for tabulating 
        headers = ["Country","Code","Product","Cost","Quantity","Value"]
        for shoes in Shoe.shoe_list:
            # Compares the product codes in object list with the user code
            if shoes[1] == product_code:
                # Once the product is found its details are added to temp_list
                temp_list.append(shoes)
                found = True
                # Display the results in a table format
                print("\n" + tabulate(temp_list,headers))
        return found
				
    def value_per_item():
        # This function adds column Value on to the data and calculates the
        # value of the items
        # Checks if the sixsth column exist
        if len(Shoe.shoe_list[0]) < 6:
            # Adds Value on the first row
            Shoe.shoe_list[0].append("Value")
        with open("inventory.txt", "w") as f:
            # Calculate value for all the items in opject list
            for item in range(1,len(Shoe.shoe_list)):
                value = float(Shoe.shoe_list[item][3]) * float(\
                    Shoe.shoe_list[item][4])
                if len(Shoe.shoe_list[item]) == 6:
                    Shoe.shoe_list[item][5] = round(value,2)
                else:
                    Shoe.shoe_list[item].append(round(value,2))
            for item in Shoe.shoe_list:
                f.write(f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]},\
{item[5]}\n")
            
# =========Main==============
# The program starts here
# Calls the function read_data() function to read all the data on the text file
Shoe.read_data()
# Calls function vulue_per_item() to calculate Value column and add it on the
# text file
Shoe.value_per_item()

while True:
    menu = input("""\nPlease select on of the following obtions:
'va'\t- to view all the shoes
'c'\t- to capture new product products
's'\t- to search product
'lq'\t- to determine product with lowest quantity
'hq'\t- to determine product with highest quantity
'e'\t- to exit
: """).lower()
    if menu == "va":
        # Displays all the data in the object list
        print(tabulate(Shoe.shoe_list))
        print("\n============================================================")
    elif menu == "c":
        # Capture new products by first checking if the alread exist
        country = input("Enter country: ")
        code = input("Enter code: ")
        # Checks if the code is already in the object file
        if Shoe.search_product(code) == True:
            print("\nThe product already exist\n")
        else:
            # If the code does not exist the proced with entering other
            # product details
            product = input("Enter product description: ")
            while True:
                try: 
                    cost = float(input("Enter cost: "))
                    quantity = int(input("Enter quantity: "))
                    break
                except ValueError:
                    print("The value you just entered is incorrect")
            # Creates shoe object
            shoe_object = Shoe(country, code, product, cost, quantity)
            # Updates the data in object list and text file
            Shoe.value_per_item()
            print("\nItem added...")
        print("\n============================================================")   
    elif menu == "s":
        # Searches for product using code
        product_code = input("Please enter product code: ")
        if Shoe.search_product(product_code) == False:
            print("\nThe code you entered does not exist")
        print("\n============================================================")
    elif menu == "lq":
        # Determines the product with lowest quantity and provides option
        # to restock it
        low_quantity = int(Shoe.shoe_list[1][4])
        product_index = 0
        for item in range(1,len(Shoe.shoe_list)):
            if int(Shoe.shoe_list[item][4]) < low_quantity:
                low_quantity = int(Shoe.shoe_list[item][4])
                product_index = item
        temp_list = []
        temp_list.append(Shoe.shoe_list[product_index])
        headers = ["Country","Code","Product","Cost","Quantity","Value"]
        print("\n" + tabulate(temp_list,headers))
        del temp_list[0]
        while True:
            stock_option = input("""\nPlease select on of the following obtions:
'rs'\t-to restock product
'rt'\t-to return to main menu
: """).lower()
            if stock_option == "rs":
                while True:
                    try:
                        quantity = int(input("Please enter quantity: "))
                        break
                    except ValueError:
                        print("That was an invalid number, please try again..")
                Shoe.shoe_list[product_index][4] = quantity
                Shoe.shoe_list[product_index][5] = int(Shoe.shoe_list\
                                                       [product_index][3]) \
                                                       * quantity
                temp_list.append(Shoe.shoe_list[product_index])
                print("\n" + tabulate(temp_list,headers))
                Shoe.value_per_item()
                break
            elif stock_option == "rt":
                break
            else:
                print("\nPlease select a correct option")
        print("\n============================================================")
    elif menu == "hq":
        # Determines the product with highest quantity and marks it
        # as it is for sale
        high_quantity = int(Shoe.shoe_list[1][4])
        product_index = 0
        for item in range(1,len(Shoe.shoe_list)):
                if int(Shoe.shoe_list[item][4]) > high_quantity:
                        high_quantity = int(Shoe.shoe_list[item][4].strip())
                        product_index = item
        temp_list = []
        temp_list.append(Shoe.shoe_list[product_index])
        headers = ["Country","Code","Product","Cost","Quantity","Value"]
        print("\n" + tabulate(temp_list,headers))
        print("\nTHIS PRODUCT IS FOR SALE")
        print("\n============================================================")
    elif menu == "e":
        print("\nGood bye!!!")
        exit()
    else:
        print("\nPlease choose a correct option")
                


