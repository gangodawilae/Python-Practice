# =====================================================================
# PROGRAM: Higher or Lower Number Guesser
# =====================================================================

# IMPORTS
import random

#Start the main game loop for the play again option
playing=True

while playing:
#Generate a number between 1 and 100 and save it in a variable
    secret_number = random.randint(1,100)
# Variable to keep track the user's current guesses
    current_guess=0

#Introduction to the game with a little discription 
print("Wlecome to the number guesser game")
print("I'm thinking a number between 1 and 100.")

#Start the game
while current_guess != secret_number:

#Ask the user to guess a number
    current_guess=int(input("\nEnter your guess:"))


#Check if the guess is too low
    if current_guess<secret_number:
        print("Too low! Try a higher number")
#Check if the guess is too high
    elif current_guess > secret_number:
        print("Too high! Try a lower number.")

# ===========================================
# EXTENSION: check if they are within 5 of secret number

    if current_guess != secret_number:
        if current_guess >= (secret_number -5) and current_guess <= (secret_number+5):
            print("Yayy, you are getting closer. You are within 5 numbers!")

#Game over with a winning message
print("Cngradulations! You have sucessfully guessed it right")

#Play again option.
#Ask the user that if they want to reapeat playing and convert input to a lowercase
user_option = input("\n Do you wants to play again? (\nYes\nNo): ").lower

#If the user don't say yes, break the loop ad end the game
if user_option != "yes" and user_option != "y":
    print("Thanks for playing my number guesser game. Bye....")

    playing= False
