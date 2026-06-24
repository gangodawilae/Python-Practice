# =====================================================================
# PROJECT: Wordle
# Create a program where the user must guess the 5 letter word.
# =====================================================================
import random
#===============================


#===============================
# FUNCTIONS
#===============================

# Run program 1:Wordle
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
            # result += f"\033[32m{guess[i]}\033[0m"

        elif guess[i] in secret:
            result += f"\033[33m{guess[i]}\033[0m"

        else:
            result += f"\033[31m{guess[i]}\033[0m"

        print("Result:", result)

print("The word was:", secret )




# # TOOLS
# # Import random so you can randomise the word
# import random

# # VALUES
# #  Create a list of at least 5 different 5-letter words
# words= ["apple", "chair", "smile", "bread"]

# play=True

# # INTRODUCTION
# # Tell your user how to play wordle (make sure they know they must input 5 letter words)
# print("Welcome to the wordle.")
# print("Guess the 5 letter word. You must enter 5 letter guesses only!")


# #Create a main loop
# while play:

#     # pick a random word
#     word= random.choice(words)

#     # USER INPUT
#     #  Get user's first guess and save it into a variable
#     guess= input("Enter your 5 letter guess: ").lower()

#     # Make sure that it is in 5 letters using len and tell them that it's not 5 letters
#     while len(guess) !=5:
#         print("That's not 5 lettters. Try again!")
#         guess=input("Enter a 5 letter word").lower()
        

#     # Check if they got it correct and if they did, tell them so and then break the loop
#     if guess == word:
#         print("Correct! You guessed the word right!.\n Good Job.")
#         again = input("Play again (yes/no): ").lower()
#         if again != "yes":
#             play = False
#         continue

    
#     # # Letter by letter checking
#     # for i in range(5):

#     #     # Check if the current letter is in the correct position
#     #     if guess[i]== word [i]:
#     #         print(guess[i], "is correct and in the right place!")

#     #     # Otherwise check if the letter is somewhere else in the word.
#     #     elif guess[i] in word:
#     #         print(guess[i], "is in the word but in the wrong place")

#     #     # Else tell them that letter is wrong
#     #     else:
#     #         print(guess[i], "is not in the word")


# # ==========================================================
# # EXTENSION

# # Instead of telling the user one by one about their letters, put each correct letter and _ for a wrong letter into a list. 
#     result = []

#     #A for loop that loops 5 times
#     for i in range(5):
#         #Check if the current letter of user_input (guess[i]) is the same as i letter of the word
#         if guess[i] == word[i]:
#             result.append(guess[i])


#         elif guess[i] in word:
#             result.append(guess[i])

#         #If not tell the user that the letter is wrong
#         else:
#             result.append("_")


#     print("Result:", "".join(result))

#     # Ask if they want to play again. If they don't, set play to false.
#     again = input("Play again?\n yes \n no: ").lower()
#     if again != "yes":
#         play= False
    
# ==========================================================
# EXPERT
# Following on from the extension, add colour to the letters instead (Don't use _ for incorrect anymore). Green for correct, orange for wrong place, red for incorrect. You'll need to add the colour as you add them to the list

# print("\033[31mThis is Red Text\033[0m")
# print("\033[38;2;255;165;0mThis is Orange Text\033[0m")
# print("\033[32mThis is Green Text\033[0m")

# Further Extension: Structure with user defined functions