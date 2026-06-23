"""
PROGRAM: Game Shop
This program runs a shop that displays user and shop inventory, can buy and sell items and displays gold.
"""

# INSTRUCTIONS
# Create functions for:
    # Displaying items
    # buy/sell function
# Display the shop menu (in main()): Buy, Sell, Exit (Give user choice and call functions based on this)



#===============================
# CONSTANTS
#===============================


#===============================
# FUNCTIONS

#All items cost 20 golds.
ITEM_PRICE=20
#===============================

# Display items with prices
# Create function called display_items with parameters: items, action
    # Loop through the items
        #Print the item name and item_price
def display_items(items,action):
    print("\n--------------------")
    print(f"Items available to {action}: ")

    #Show items with prices
    for item in items:
        print(f"{item}({ITEM_PRICE} gold)")

    print("\n Type the item name to choose it.")
    print("\n Or print 'exit' to go quit")


#Ask user repeadetly until valid choices
 # reate an infinite while loop
#Ask the user which item they'd like to (action)
    while True:
        choice = input(f"What would you like to {action}?").strip()
    

        # If the user's input is equal to  'EXIT', return 
        if choice == "Exit":
            #return
            return None

        #We use "in" statement and see, and check if items exsists.
        for item in items:
            if choice == item:
                return item
            
        print("That item is not available.")


# Run main code
def main():
    #Shops starts with items
    shop_items = ["Sword","Shield","Potion","Bow"]

    #Create an empty list of inventory items
    inventory=[]
    
    #Create a gold variable and set it to 500
    gold=500

    # Welcome the player to the shop
    print("Welcome to the game shop!!")


    # Create an infinite while loop
    while True:
        #This is show the shop menu, including buy, sell, and exit. 
        print("Shop menu")
        print("1.Buy")
        print("2.Sell")
        print("3.Exit")

        
        choice=input("Choose an option:").strip()
        
        if choice == "3":
            break

        elif choice == "1":
            item=display_items(shop_items,"buy")

            if item is not None:
                if gold>= ITEM_PRICE:
                    inventory.append(item)
                    shop_items.remove(item)
                    gold -= ITEM_PRICE

                    print(f"\nYou bought {item}")
                    print(f"Gold left: {gold}")
                else:
                    print("You don't enough money")

        elif choice == "2":
            if len(inventory) == 0:
                print("You have nothing to sell!")
                continue

            item=display_items(inventory,"sell")

            if item is not None:
                shop_items.append(item)
                inventory.remove(item)
                gold += ITEM_PRICE
                print(f"\n You sold {item}")
                print(f"Gold now, {gold}")

            else:
                print("Invalid choice. Maybe try again!!!!!")

        print("\nThanks for visiting my shop. Good Byeeeee")
        


#===============================
# EXECUTION
#===============================

# Execute main cod
main()



#===============================
#===============================
# EXTENSION
# Create dictionaries for each item for flexibility and to display other info: attack, defence, item_description