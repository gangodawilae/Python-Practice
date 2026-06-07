# =====================================================================
# PROGRAM: Age verification
#           Verify the user's age is over 18 to give access (or deny access)
#           Keep asking for input until they've given a valid age
# =====================================================================

# VARIABLES
# TODO Create a variable for valid input and set it to false
is_valid_input=False
# GET INPUT
while not is_valid_input:
    user_input=input("Please enter your age: ")

  #TRY to convert
    try:
        age= int(user_input)
        is_valid_input=True
  
    #Fail to convert to integer part
    except:
        print("Invaid input!!! Please enter a numeric number for your age")

#Check age
    if age>=18:
        print("\nAccess accepted. Full access for you! ")
    elif age>=13:
        print("\n Partcial access accepted ")
    else: 
        print("\n You must be at least 13 to access. Access denied.")


# ===================================================================
# EXTENSION
# Create a avatar creator for them to use if they get access. There should be 2 versions (full and partial)
# Eg. Full can choose: character class (warrior, rogue), hair colour, eye colour; partial just character class (with animal classes?)




