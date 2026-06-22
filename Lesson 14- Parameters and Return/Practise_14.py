"""
PROGRAM: Geometry Helper
This program helps to calculate the area and perimeter of a rectangle
"""

####### INSTRUCTIONS ########
# Complete the code by writing functions for calculating the area and perimeter 
# taking the user input and returning it, 
# and calling each function based on user choice


# =====================================================================
# FUNCTIONS

def calculate_area(length,width):
    area=length*width
    return area

#Calculate perimeter
def calculate_perimeter(length,width):
    perimeter= 2* (length+width)
    return perimeter
# =====================================================================


def display_result(message):
    print("\n------------------")
    print(message)
    print("------------------")

# Run the main program
def main():

    print("Welcome to the Geometry Helper for rectangles!\n")
    print("1. Area Calculator")
    print("2. Perimeter Calculator")

    length = int(input("What is the length of your rectangle?").strip())
    width = int(input("What is the width of your rectangle?").strip())

    choice = input("\nWhich tool do you want to use? (1 or 2): ").strip()

    # Trigger function based on user choice
    if choice == "1":
        result = calculate_area(length,width)
        display_result(f"The area is {result} sqaure units.")
    
    elif choice == "2":
        result=calculate_perimeter(length,width)
        display_result(f"The perimeter is {result} units.")

    else:
        print("Invalid choice. Please enter proper numbers.")
main()