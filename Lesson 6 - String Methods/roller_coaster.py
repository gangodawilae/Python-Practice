# Create a roller coaster access screener (determine if the user is allowed to ride)
# Rules:    They must be over 150cm and over 10 years old
#           They must not have a heart condition
#           OR they can ride if they have a VIP pass

#Ask which ride the user wants
ride=input("Which ride do you want?(A, B, or C): ").upper()

# Get input

height=int(input("Enetr your height in cm:"))
age=int(input("Enetr your age:"))
conditions=input("Do you have a heart condition?\n (yes/no):" ).lower()
vip=input("Do you have a VIP password?\n (yes/no):").lower()



# Check conditions and output verdict
if vip=="yes":
    print("Access guranteed")
else:
    #1st ride rules

    if ride=="A":
       if height>150 and age>10 and conditions=="no":
           print("Access guranteed for your first ride which is Fear Drop") 


   #2nd ride rules
    elif ride == "B":
        if height>140 and age>12:
            print("Access gurenteed for our second ride which is bumper boats")
    else:
        print("Access denied for ride B")

   #3rd ride rules
    elif ride == "C":
        if height > 120 and age > 8 and conditions == "no":
            print("Access gurenteed for our second ride which is scorpian karts")
        else:
            print("Access dened for ride C")


# elif height>150 and age>10 and conditions=="no":
#     print("Access guranteed")
# else:
#     print("Access denied")


# ------------------------------
# EXTENSION
# Change your screener to work for 3 different rides (ask user which ride at the beginning) with different rules

# ------------------------------
# EXPERT
# Follow the same task (with extension), but use dictionaries to make the code more efficient