"""
PROGRAM: Menu
This starts with a menu so users can run 1 of 3 different programs:
1.
2.
3.
"""

#===============================
# IMPORTS
#===============================

# TODO Once you've copied your 3 programs below, move any imports to here

#===============================
# FUNCTIONS
#===============================

#Create a funtion to hold your first program 
def run_program_one():

    # Paste the code fo your first program
    print("You are running progra 1.")


#Create a funtion to hold your second program. 
def run_program_two():
    #  Copy and paste the programs code inside (meaning indented)
    print("You are running program 2.")


# Create a function to hold your third program. 
def run_program_three():
    # Copy and paste the programs code inside (meaning indented)
    print("You are running program 3.")


#Create a main function
#Introduce the menu and output options
def main():
    print("Program menu.")
    print("1. Run program 1.")
    print("2. Run Program 2.")
    print("3. Run Program 3.")
    
    # Ask user which program they'd like to run and store input in a variable
    choice=input("Which program whoud you like to run? (Please enter 1,2, or 3): ")

    # Check if they said "1" (with speech marks)
    if choice == "1":
        #Call program 1 function
        run_program_one()

    #Otherwise check if they said "2" (with speech marks)
    elif choice == "2":
         #Call program 2 function
         run_program_two()

    # Otherwise check if they said "3" (with speech marks)
    elif choice == "3":
        #Call program 3 function
        run_program_three()
    
    else:
        print("Invaid choice Please restart the program and enter 1,2, or 3")


#===============================
# EXECUTION
#===============================

# TODO Call main function

if __name__ == "__main__":
    main()

#===============================
#===============================
# EXTENSION
# TODO Go back to each program you chose and structure them with functions. 
# TODO Then recopy them over as multiple functions (rather than one)
# NOTE The main() function in your programs can be renamed as run_program_name() so it doesn't clash with this program's main()