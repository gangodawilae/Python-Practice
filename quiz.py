#Starts with 0 points
score =0
print("Hello!")
print("Welcome to my quiz game!")
print("Choose the correct option,(a, b, or c)")
input("Are you ready...?")
print("Let's start!!, I believe in you")

#Question 1 with answers
print("1. who is the first person to space?")
print("a) Yuri Gagarin")
print("b)Thomas Eddison")
print("c)Neil Armstrong")
answer=input("Your answer: ")
if answer == "a":
   print("correct!")
   score= score + 1
else:
   print("Wrong. The answer is a")

#Question 2 with answers
print("2. Which bird can fly backward?")
print("a) Blue duck")
print("b)Hummingbird")
print("c) Butterfly")
answer=input("Your answer: ")

if answer == "b":
   print("Correct!")
   score= score + 1
else:
   print("Wrong.The answer is b")

#Question 3 with answers
print("3. What is the nation bird of New Zealand?")
print("a)kiwi")
print("b)Tui")
print("c)Ruru")
answer=input("Your answer: ")
if answer == "a":
   print("Correct!")
   score= score + 1
else:
   print("Wrong. The answer is a")

#Question 4 with answers
print("4. Where is Mount Olympus located")
print("a)Rome")
print("b)Russia")
print("c)Greece")
answer=input("Your answer: ")
if answer == "c":
   print("Correct!")
   score= score + 1
else:
   print("Wrong. The answer is c.")

#Question 5 with answers
print("5. What does cows drink?")
print("a)Water")
print("b)Milk")
print("c)Tea")
answer=input("Your answer: ")
if answer == "a":
   print("Correct!")
   score= score + 1
else:
   print("Wrong. The answer is a." )

#Question 6 with answers
print("6. What is 128+22-5")
print("a)117")
print("b)35")
print("c)145")
answer=input("Your answer: ")
if answer == "c":
   print("correct!")
   score= score + 1
else:
   print("Wrong. The answer is c.")

#Question 7 with answers
print("7.What is the diffrence between object mode and edit mode in blender?")
print("a)Object mode is for animating and edit mode is for texturing")
print("b)Object mode is for modelling and edit mode is for moving objects around ")
print("c) Modelling like positioning,rotating adding objects and edit mode is modifying of a object's internal geomatry like moving, and deleting vertices,edges,and faces and etc. ")
answer=input("Your answer: ")
if answer == "c":
   print("Correct!")
   score= score + 1
else:
   print("Wrong.The correct answer is c")

#Question 8 with answers
print("8.Which one is the largest planet?")
print("a)Saturn")
print("b)Jupiter")
print("c)Sun")
answer=input("Your answer: ")
if answer == "b":
   print("Correct!")
   score= score + 1
else:
   print("Wrong, the correct answer is b")

#Question 9 with answers
print("9. What is the largest organ in the human body?")
print("a)Skin")
print("b)Heart")
print("c)Lungs")
answer=input("Your answer: ")
if answer == "a":
   print("Correct!")
   score= score + 1
else:
   print("Wrong. The answer is a")

#Question 10 with answers
print("10.What is the smallest unit of matter")
print("a)Molecule")
print("b)Atom")
print("c)Proton")
answer=input("Your answer: ")
if answer == "b":
   print("Correct!")
   score= score + 1
else:
   print("Wrong. The answer is b.")

#Scoring
print("\nYou got", score, "correct out of 10")

#Conclution part
print("Yay! I sure that you got most of them correct, may be all")
print("Thanks for playing my game")