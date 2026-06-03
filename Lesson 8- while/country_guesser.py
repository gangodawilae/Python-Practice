# =====================================================================
# Task: Country Guessing Game
# =====================================================================



#  VALUES
correct_country = "Italy"
current_guess = ""

print("Welcome to my country guesser game")
print("\n Here..You need to guess the correct country name")
# LOOP
while current_guess != correct_country:
    current_guess = input("What is the correct country? ")
    
    # Optional: Encourage the user or give a hint
    if current_guess.lower() != correct_country.lower():
        print("Not quite! Try thinking of a famous boot-shaped country.")
        
# GAME OVER / WINNING MESSAGE
print("Congratulations! You guessed it!")
# ================================================================
# EXTENSION
# TODO: Add an introduction
# TODO: Add a scoring system (starts at 20, lose 1 point for each wrong guess)
# TODO: Agdd a lose condition (if score reaches 0)

#==================================================================
# EXPERT
# TODO: Make the game unique (use a list of countries and randomly select one)
# TODO: Add a play again option

