# =====================================================================
# PROJECT: The Magic 8-Ball Fortune Teller
# Create a program that gives random responses to yes/no questions
# =====================================================================

# TOOLS
# TODO: Import the 'random' module so we can pick a random index later.
import random

# RESPONSES
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
        break

    # RANDOM REPSONSE
    # TODO: Step A: Calculate the last valid index of your list.
    #       (Remember: If a list has 5 items, the indexes are 0, 1, 2, 3, 4).
    #       Use random.randint() to get a number between 0 and that last index.
    #       Save it in a variable called 'random_index'.
    chance = random.random()

    #Check if the number is lower than 0.8 and use the common list
    if chance <0.8:
        chosen_fortune = random.choice(common_responses)

    
    #Otherwise use the rare list
    else:
        chosen_fortune = random.choice(rare_responses)

    # TODO Print the result
    print("Magic 8 ball says..:", chosen_fortune )

# TODO Say goodbye to let them know the program has ended.
print("Good Bye")


# EXPERT
# Try creating a magic eight ball that gives random responses based on the question (eg. positive, negative, snarky, funny responses)
# TODO Create a dictionary (or multiple lists)
# TODO Check for key words in the question to decide what type of response. Eg. "will I" has positive responses, short questions have snarky responses, "think" has funny responses, etc.