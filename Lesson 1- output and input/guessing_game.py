print("Welcome to the Guesssing Game!! Yayyy")
print("I'm thinking of word...")

answer="age"

guess1=input("Hint 1:\nIt's a thing in the world that everybody has, but nobody can ever give it away. \nYour answer:")

if guess1.lower() == answer:
    print("\nGood job! You got it on the first try!")
else:
    print("\nOhh, it's not the word.. but I can give you the second clue.\n")

guess2=input("Hint 2:\nIt's a reason why some people are called juniors and others are called seniors.\nYour answer:  ")
if guess2.lower() == answer:
    print("\nCorrect! You guessed it!")
else:
    print("\nIt's not the answer. But I believe in you!!.\n")

guess3=input("Hint 3:\nYou have to blow certain amount of candles ona cake because of this.\nFinal answer: ")
if guess3.lower() == answer:
    print("\nYou've got it right. Look I always believed in you")
else:
    print("\nAwww, the answer was:", answer)


 
