import csv

def main():
    
    while True:
        print("\n[Main Menu]")
        print("1 - Add new item\n2 - Show the inventory\n3 - Search for item\n0 - Exit")
        try:
            selection = int(input("Select: "))
            if selection in (0, 1, 2, 3):
                if selection == 1:
                    add_new_item()
                elif selection == 2:
                    show_inventory()
                #elif selection == 3:
                    #search_inventory(filename)
                else:
                    break
        except:    
            print("Error: Input a valid value.")
            
def add_new_item():
    handtools = "Handtools.csv"
    powertools = "powertools.csv"
    while True:
        print("Is your item a (1)Hand tool or (2)Power tool?")
        try:
            selection = int(input("Select a number: "))
            if selection in (0, 1, 2):
                if selection == 1:
                    add_hand(handtools)
                elif selection == 2:
                    add_power(powertools)
                else:
                    break
        except:
            print("Error: Input a valid value.")
      
def add_hand(handtools):
    hinvevntory = get_records(handtools)
    
    valid = True
    try:
        category = input("What kind of hand tool: ?")
        name = input("Name of tool: ")
        desc = input("Short description of tool: ")
        count = int(input("Amount of item: "))
        code = int(input("Designate a code for this item: "))
        
        new_handtool = [category, name, desc, count, code]
        hinventory.append(new_handtool)
    except:
        valid = False
        print("Error: Input a valid value.")
    
    if valid:
        with open(handtools, "w+", encoding="utf-8", newline="") as hfile:
            writer = csv.writer(hfile)
            for item in inventory:
                writer.writerow(item)
        print(f"Succesfully added '{name}' to the hand tools inventory.")

def add_power(powertools):
    pinvevntory = get_records(powertools)
    
    valid = True
    try:
        category = input("What kind of hand tool: ?")
        name = input("Name of tool: ")
        desc = input("Short description of tool: ")
        count = int(input("Amount of item: "))
        code = int(input("Designate a code for this item: "))
        
        new_powertool = [category, name, desc, count, code]
        hinventory.append(new_powertool)
    except:
        valid = False
        print("Error: Input a valid value.")
    
    if valid:
        with open(powertools, "w+", encoding="utf-8", newline="") as pfile:
            writer = csv.writer(pfile)
            for item in inventory:
                writer.writerow(item)
        print(f"Succesfully added '{name}' to the power tools inventory.")

def show_inventory(filename):
    inventory = sorted(get_records(filename))
    
    item_count = len(inventory)

    print(f"\n[Inventory - {item_count} item(s)]")

    for item in inventory:
        category = item[0]
        name = item[1]
        desc = (item[2])
        count = int(item[3])
        code = (item[4])
        print(f" {category} - {name}, {desc}, x{count}, {code} ")

def get_records_ht(handtools):
    with open(handtools, "r", encoding="utf-8") as hfile:
        return list(csv.reader(hfile))
        
def get_records_pt(powertools):
    with open(powertools, "r", encoding="utf-8") as pfile:
        return list(csv.reader(pfile))        
            
if __name__ == "__main__":
    main()