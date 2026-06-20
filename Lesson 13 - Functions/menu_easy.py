"""
PROGRAM: Menu
This starts with a menu so users can run 1 of 3 different programs:
1.
2.
3.
"""

#===============================
# IMPORTS
import random
#===============================


# Run program 1:Wordle
def run_wordle():
    words = ["apple","chair","smile","bread"]
    secret = random.choice(words)

    print("\n Welcome to the..... Wordle!!")
    print("Guess the 5 letter word. You must enter 5 letter guesses only.\n Type 'quit' to exit.")

    while True:
        guess= input("Enter your guess: ").lower()


        if guess == "quit":
            print("Goodbye")
            break

        if len(guess) != 5:
            print("Guess must be 5 letters!")
            continue

        if guess == secret:
            print("\033[32mCorrect! You guessed the word!\033[0m")
            break

        result = ""
        for i in range(5):
            if guess[i] == secret[i]:
                result += f"\033[32m{guess[i]}\033[0m"

            elif guess[i] in secret:
                result += f"\033[33m{guess[i]}\033[0m]"

            else:
                result += f"\033[31m{guess[i]}\033[0m]"

        print("Result", result)

    print("The word has:", secret )

# Run program 2: Magic 8 Ball

def run_magic_8ball():
    print("Welcome to...... \n Magic-8 ball!!")

# TODO: Create a list called 'responses' that contains at least 8 different responses.
    common_responses = ["Yes, definetly",
             "Absolutly",
             "Yeah, probably",
            "I'm not sure",
             "Could be",
             "No, definetly not",
             "Maybe... but try again later",
             "I guess soo...",
             "Not really sure yet"]

    rare_responses = ["I don't think so...",
                  "Honestly, I have no idea",
                  "Ummm. I don't think I should answer that question",
                  "I'm not sure about that one",
                  "Ask me that again another day",
                  "Hmmm. That's a tough one to answer actually"]

# MAIN LOOP
# TODO Create an infinite loop
    while True:
        question=input("Ask a yes/no question about your future (or type 'quit' to leave): ")
    
    # Check if the user wants to exit and break from the loop if they do.
        if question.lower() == "quit":
            print("Good bye!!")
            break

    
        chance = random.random()

    #Check if the number is lower than 0.8 and use the common list
        if chance <0.8:
            chosen_fortune = random.choice(common_responses)

    
    #Otherwise use the rare list
        else:
            chosen_fortune = random.choice(rare_responses)

        #Print the result.
        print("Magic 8 ball says..:", chosen_fortune )



# Run program 3: Pokemon battle
# =====================================================================
# PROJECT: Pokemon
# Create a battle program where you battle a random pokemon
# =====================================================================

def run_pokemon():
    print("Welcome to......\n Pokemon Battle!!")

# Wild Pokemon
# Create a multidimensional list that holds 4 pokemon names and their max health (you choose)
    wild_pokemon = [
        {"name":"pikachu","health": 60},
        {"name":"Charmander","health":55},
        {"name":"Squirtle","health":65},
        {"name":"Bulbasaur","health": 70}
    ]
# User Pokemon
# Create a multidimensional list that holds 4 pokemon attacks and their different damage
    user_attacks=[
        {"move":"Tackle","damage":10},
        {"move":"Thunderbolt","damage":15},
        {"move":"Quick Attack","damage":12},
        {"move":"Mega punch", "damage":20}
    ]

#  Create a variable to hold a randomised wild pokemon
    enemy= random.choice(wild_pokemon)
    current_health=enemy["health"]

    print(f"A wild {enemy['name']} appeared! It has the {current_health} health points. ")

#Battle loop
    while current_health>0:

    #Show attack options
        print("\nChoose your attack:")
        for i in range(len(user_attacks)):
            print(f"{i+1}. {user_attacks[i]['move']} ({user_attacks[i]['damage']} damage)")

    #Get user's input
        choice=input("Please enter attack number:")

    #  Use try except to ensure the user has input a number; if they didn't tell them so and then use 'continue' to restart the loop
        try:
            choice=int(choice)-1
            if choice<0 or choice >= len(user_attacks):
                continue
        except:
            print("Please enter a number:")
            continue

    #Apply damage
        damage=user_attacks[choice]["damage"]
        current_health-=damage

        print(f"You used {user_attacks[choice]["move"]}")

    #Show remaining health
        if current_health>0:
            print(f"{enemy["name"]} has {current_health} health points left ")
        else:
            print(f"{enemy["name"]} has 0 health points left")
            print(f"\n Yayyy. You defeated the wild {enemy["name"]}. Good Job! ")

# TODO Once you've copied your 3 programs below, move any imports to here

#===============================
# FUNCTIONS
#===============================


#Create a main function
#Introduce the menu and output options
def main():
    print("Program menu.")
    print("1. Wordle")
    print("2. Magic 8-ball.")
    print("3. Pokemon Battle")
    
    # Ask user which program they'd like to run and store input in a variable
    choice=input("Which program whoud you like to run? (Please enter 1,2, or 3): ")

    # Check if they said "1" (with speech marks)
    if choice == "1":
        run_wordle()

    #Otherwise check if they said "2" (with speech marks)
    elif choice == "2":
         run_magic_8ball()

    # Otherwise check if they said "3" (with speech marks)
    elif choice == "3":
        run_pokemon()
    
    else:
        print("Invaid choice. Please restart the program and enter 1,2, or 3")


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