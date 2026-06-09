# =====================================================================
# PROJECT: The Magic 8-Ball Fortune Teller
# Create a program that gives random responses to yes/no questions
# =====================================================================

# TOOLS
# TODO: Import the 'random' module so we can pick a random index later.
import random

# RESPONSES
# TODO: Create a list called 'responses' that contains at least 8 different responses.
responses = ["Yes, definetly",
             "Absolutly",
             "Ask again later",
             "I don't thin soo..",
             "No, definetly not",
             "Maybe... bu try again later",
             "Outlook not so good",
             "Ask again later"]

# MAIN LOOP
# TODO Create an infinite loop
while True:
    question=input("Ask a yes/no question about your future (or type 'quit' to leave): ")
    
    # Check if the user wants to exit and break from the loop if they do.
    if question.lower() == "quit":
        break

    # RANDOM REPSONSE
    # TODO: Step A: Calculate the last valid index of your list.
    #       (Remember: If a list has 5 items, the indexes are 0, 1, 2, 3, 4).
    #       Use random.randint() to get a number between 0 and that last index.
    #       Save it in a variable called 'random_index'.
    last_index=7
    random_index = random.randint(0, last_index)
    
    # TODO: Step B: Use your 'random_index' to grab the matching answer 
    #       out of your 'responses' list.
    #       Save it in a variable called 'chosen_fortune'.
    chosen_fortune=  responses[random_index]

    # TODO Print the result
    print("Magic 8 ball says..:", chosen_fortune )

# TODO Say goodbye to let them know the program has ended.
print("Good Bye")

# ==================================================
# EXTENSION
# Common and rare responses
# TODO Split your responses into 2 lists. A common responses list and a rare responses list
# TODO Use random.random() or randint() to get a percentage
# TODO Check if the number is lower than 0.8 and use the common list to give a response if it is
# TODO Otherwise use the rare list

# ===================================================
# EXPERT
# Try creating a magic eight ball that gives random responses based on the question (eg. positive, negative, snarky, funny responses)
# TODO Create a dictionary (or multiple lists)
# TODO Check for key words in the question to decide what type of response. Eg. "will I" has positive responses, short questions have snarky responses, "think" has funny responses, etc.