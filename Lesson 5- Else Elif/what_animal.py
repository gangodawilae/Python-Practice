### WHAT ANIMAL ARE YOU QUIZ ###

# FIRST, create a basic Flowchart using the FLowchart Shapes to plan the flow of your 'what animal are you' quiz. 
# __________________________

# Write a 'what animal are you' quiz. 
print("Welcome to, 'what animal you are!' quiz")


# Question 1
choice1=input("Do you prefer, \n1)Day \n2)Night")
# If they prefer day
if choice1 == "1":
    # Question 2
    choice2=input("Do you prefer, \n1)Swim \n2)Run")

    #If they prefer run
    if choice2 == "2":
        print("You are a cheetah!")
    elif choice2 == "1":
        print("You are a dolphin!")
    else:
        print("Please enter choice 1 or choice 2")

elif choice1 == "2": 
    #Question 3
    choice3= input("Do you prefer, \n1)Glow in the dark? \n2)Make loud noices? ")


    if choice3 == "1":
        print("You are a firefly!")
    elif choice3 == "2":
        print("You are a cricket!")

        #Question 4
        choice4= input("Do you like to, \n1) Hunt \n2)Hide")
        if choice4 =="1":
            print("You are a wolf!")
        elif choice4 == "2":
            print("You are a owl!")
        else:
            print("Please enetr your choice number")

        #Qoestion 5
    choice5 = input("Do you prefer to eat, \n1) Leaves high up? \n2)Roots and grass")
    if choice5 == "1":
        print("You are a koala!")    
    elif choice5 == "2":
        print("You are a rabbit!")   
    else:
        print("Plese enter 1 or 2")  
else:
    print("Please choose 1 or 2 option")   
# __________________________

# EXTENSION
# Extend the quiz so there are 8 possible animals
# Create a Flowchart using the FLowchart Shapes to 

# __________________________

# EXTENSION 2
# Create a 'Which ??? are you?' Quiz
# This time allow all questions to have 4 possible answers (a,b,c and d) 
# and tally how many times they choose each
# Determine what they are at the end using the letter with the highest tally.
# Eg. If they picked mostly As, maybe they are Pikachu.