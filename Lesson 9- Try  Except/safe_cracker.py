# =====================================================================
# PROGRAM: Safe Cracker (The Digital Vault)
# =====================================================================

# SETUP YOUR VARIABLES
correct_conbination="742"
attempts=0
max_attempts=5


# INTRODUCE THE GAME
print("Welcome to safe cracker")
print("\nHere, you are trying to hack the high-security vault.")
print(f"You are {max_attempts} attempts before the alarm ring")
print("\nType 'exit' to quit the game entirely at any time")


# LOOP
while True:
    #Ask the user to enter a 3 digit combination
    user_input= input("Enter the 3 digit combination").strip()


    # -----------------------------------------------------------------
    # SCENARIO A: The user wants to quit
    # -----------------------------------------------------------------
    if user_input.lower()== "exit": 
        print("Aborting mission...")
        break

# -----------------------------------------------------------------
    # SCENARIO B: Invalid Input
    # -----------------------------------------------------------------
    try:
        int(user_input)
    except:
        print("Error is occuring. Safe only accepts digits. Try again")
        continue

    # -----------------------------------------------------------------
    # SCENARIO C: Processing a valid attempt
    # -----------------------------------------------------------------
    #Increase attempts tracker varibale by 1
    attempts+=1

    #Check weather the user inpu matches the correct vault combination
    if user_input == correct_conbination:
        print("Vault unlocked! You found the treasure")
    #Exist teh loop because they won
    else:
        print("Combination faied. May be try again ")


#Scenerio D: the extention part.
    if attempts>= max_attempts:
        print("Alarm triggered. Security is on the way!")
    #Exsit the loop because they lost 

# ---------------------------------------------------------------------
print("\n--- Game Over ---")



