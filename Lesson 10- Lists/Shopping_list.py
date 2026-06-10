# =====================================================================
# PROJECT: Shopping List & Budget Tracker
# GOAL: Practice adding items to lists and calculating data from them.
# =====================================================================

# INITIALIZE YOUR LISTS
# TODO: Create an empty list called 'shopping_cart' to hold item names.
shopping_cart= []
# TODO: Create an empty list called 'price_list' to hold item prices.
price_list= []
budget=20
# MAIN
# TODO Create an infinite while loop
while True:
    # Info for user
    print("\n Your current cart:", shopping_cart)
    print("Current prices:", price_list)
    budget+=1


    # TODO Output Options for user: 1. Add item to cart, 2. Remove item from cart, 3. Clear cart and restart, 4. View total and checkout
    print("\n Choose an option:")


    menu_options = [
        "1. Add item to cart",
        "2. Remove item from cart",
        "3. Clear cart and restart",
        "4.View total checkout"
        ]
    for option_text in menu_options:
        print(option_text)
    # TODO Get user input (1-4) and save in variable
    option= input("Enter 1,2,3 or 4: ")
    # -----------------------------------------------------------------
    # OPTION 1: ADD ITEM 
    # -----------------------------------------------------------------
    if option == "1":

        # Ask user for the name of the item
        item= input("Please enter the item name: ")
        # Add it to shopping list
        shopping_cart.append(item)
        # Add user for price of item
        price= input("Please enter the price of the item: ")
        # Change price into a float
        price = float(price)
        # Add price to price list
        price_list.append(price)

        print(item, "added to the cart!")

    # -----------------------------------------------------------------
    # OPTION 2: REMOVE ITEM 
    # -----------------------------------------------------------------
    # Else check if option 2
    elif option == "2":
        #  Ask user for the name of the item they want to remove
        item_to_remove= input("Enter the item you want to remove:")

        if item_to_remove in shopping_cart:
        # Use .index() to get the index of the item and save in variable
            index = shopping_cart.index(item_to_remove)
        # Remove the item from cart
            shopping_cart.pop(index)
        #  Remove the price (using its index) from the price list
            price_list.pop(index)

            print(item_to_remove, "is removed")
        else:
            print("That item is not in your cart")

    # -----------------------------------------------------------------
    # OPTION 3: CLEAR CART (Practice clearing a list)
    # -----------------------------------------------------------------
    #  Else check if option 3
    elif option == "3":
        # Use the .clear() method on both lists to empty them out.
        shopping_cart.clear()
        price_list.clear()
        # Tell them their cart is empty.
        print("Your cart is now empty")


    # -----------------------------------------------------------------
    # OPTION 4: CHECKOUT
    # -----------------------------------------------------------------
    #  Else check if option 4
    elif option == "4":
        total_cost = sum(price_list)
        
        # TODO Display the results
        print("\nCheck out summery")
        print("\nItems:", shopping_cart)
        print("Prices:", price_list)
        print("\nTotal cost: $", total_cost)
        # TODO Exit the loop (to exit the program)
        break

    # -----------------------------------------------------------------
    # NO OPTION
    else:
        print("Your option isn't valid. Please enter valid options.")

# ====================================================================
# EXTENSION
# Add a budget to the list
# TODO Tell them if their cart is over budget
# TODO Recommend items to remove based on their price.

# =====================================================================
# EXPERT
# Change your program to use dictionaries so prices are connected to shopping items
# Display the cart in alphabetical order
# Add an option to display the cart in order of price.