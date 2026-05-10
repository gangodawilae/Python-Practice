# Create a short Madlib: Get input from your user (a bunch of words), 
# then output a madlib using those words.

# Ask user for a name and save it in a variable
name=input("\nplease enter your name:")
# adjective= input ("Enter an adjective (describing the name):")
# place=input("Enter a place:")

# Ask user for an animal and save it in a variable
animal=input("please enter a animal name:")

# Ask user for a colour and save it in a variable
color=input("please enter a color:")


# Ask user for an object and save it in a variable
object=input("please enter a object name:")

# Print your madlib using the 4 variables above.
print(f"One bright morning,{name} woke up to a strange sound outside.")
print(f"It wasn't a bird. It wasn't the wind.")
print(f"It was a {animal} running in circles, shouting.'Help! The colors are disappearing!'")
print(f"Sure enough, the sky was turning grey, the trees were fading, and even the flowers looked sleepy.")
print(f"The {animal} held up a glowing {object}. 'This is the color keeper,' it said. 'But it only works when someone brave chooses a special color.'")
print(f"Without thinking, {name} whispered their favourite color which was {color} Suddenly, WHOOSH! Ahuge swirl of {color} light burst from the {object}, shooting across the sky like fireworks.")
print(f"The trees brightened. The flowers sparkled. Even the clouds looked like they were smiling.")
print(f"'You did it!' the {animal} cheered. 'You saved the world of color!'. Before {name} coud reply, the magical {object} floated into their hands, glowing softly as if waiting for the next adventure")

# EXTENSION
# Research about 'print formatting in python'. 
# Use what you learn to rewrite your madlib into easier to read code.

# ----------------------------

# EXPERT (for those who already know some Python)
# Create a randomised madlib game
# GOAL: Just like above except...
#       Write 4-6 different madlibs and randomise which one is output.