# =====================================================================
# PROJECT: Pokemon
# Create a battle program where you battle a random pokemon
# =====================================================================

# Import random module
import random

# Wild Pokemon
# Create a multidimensional list that holds 4 pokemon names and their max health (you choose)
wild_pokemon = [
    {"name":"pikachu","health": 60},
    ["Charmander", 55],
    ["Squirtle",65],
    ["Bulbasaur", 70]
]
# User Pokemon
# Create a multidimensional list that holds 4 pokemon attacks and their different damage
user_attacks=[
    {"move":"Tackle","damage":10},
    ["Thunderbolt", 15],
    ["Quick Attack", 12],
    ["Mega punch", 20]
]

#  Create a variable to hold a randomised wild pokemon
enemy= random.choice(wild_pokemon)

# Set current health to the pokeman's max health
current_health=enemy["health"]
print(f"A wild {enemy['name']} appeared! It has the {current_health}. ")

#Battle loop
while current_health>0:

    #Show attack options
    print("\nChoose your attack:")
    for i in range(len(user_attacks)):
        print(f"{i+1}. {user_attacks[i]["move"]} ({user_attacks[i]["damage"]} damage)")

    #Get user's input
    choice=input("Please enter attack number:")

    #  Use try except to ensure the user has input a number; if they didn't tell them so and then use 'continue' to restart the loop
    try:
        choice=int(choice)-1
        if choice<0 or choice >= len(user_attacks):
            continue
    except:
        print("Please neter a number:")
        continue

    #Apply damage
    damage=user_attacks[choice]["damage"]
    current_health-=damage

    print(f"You need {user_attacks[choice]["move"]}")

    #Show remaining health
    if current_health>0:
        print(f"{enemy[0]} has {current_health} health points left ")
    else:
        print(f"{enemy[0]} has 0 health points left")
#End of the battle
print(f"\n Yayyy. You defeated the wild {enemy[0]}. Good Job! ")

# ====================================================
# EXTENSION
# NOTE: Only do the extension once you have completed the project update (with dictionaries)

# TODO: Give your wild pokemon each an attack value as well, then allow it to attack the user back each turn (You'' need a player health)
# TODO: Change your 'user pokemon' to a list of different pokemon they can choose from. Each pokemon will have their own list of attacks.
# TODO: Give all pokemon a type. Create a new dictionary of types that each has a dictionary of strengths and weaknesses. Use this to change the damage.