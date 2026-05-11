#Starts with 0
score = 0
print("Hello!")
print("Welcome to my quiz game!")
print("Choose the correct option,(a, b, or c)")

#Question 1 with answers
print("1. who is the first person to space?")
print("a) Yuri Gagarin")
print("b)Thomas Eddison")
print("c)Neil Armstrong")
answer=input("Your answer: ")
if answer == "a":
   score= score + 1

#Question 2 with answers
print("2. Which bird can fly backward?")
print("a) Blue duck")
print("b)Hummingbird")
print("c) Butterfly")
answer=input("Your answer: ")
if answer == "b":
   score= score + 1

#Question 3 with answers
print("3. What is the nation bird of New Zealand?")
print("a)kiwi")
print("b)Tui")
print("c)Ruru")
answer=input("Your answer: ")
if answer == "a":
   score= score + 1

#Question 4 with answers
print("4. What is Mount Olympus located")
print("a)Athens")
print("b)Russia")
print("c)Greece")
answer=input("Your answer: ")
if answer == "c":
   score= score + 1

#Question 5 with answers
print("5. What does cows drink")
print("a)Water")
print("b)Milk")
print("c)Tea")
answer=input("Your answer: ")
if answer == "a":
   score= score + 1

#Question 6 with answers
print("6. What is 128+22-5")
print("a)117")
print("b)35")
print("c)145")
answer=input("Your answer: ")
if answer == "c":
   score= score + 1

#Question 7 with answers
print("7.What is the diffrence between object mode and edit mode?")
print("a)Object mode is for animating and edit mode is for texturing")
print("b)Object mode is for modelling and edit mode is for moving objects around ")
print("c) Modelling like positioning,rotating adding objects and edit mode is modifying of a object's internal geomatry like moving, and deleting vertices,edges,and faces and etc. ")
answer=input("Your answer: ")
if answer == "c":
   score= score + 1
print("\nYou got", score, "correct out of 10")