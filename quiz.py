#Total question number inside a cosntant
TOTAL_QUESTIONS = 11

#Starts with 0 points
score =0

#Ask for users's name
user_name=input("Hello! What is your name?").strip().title()

#Start of the quiz with a welcome to my quiz
print(f"Welcome to my quiz game! {user_name}")
print("Choose the correct option,(a, b, or c)")
input("Are you ready...? Press yes to start")
print(f"\nLet's start!!, I believe in you, {user_name}!")


#Question 1
print("\n1. who is the first person to space?")
print("a) Yuri Gagarin")
print("b)Thomas Eddison")
print("c)Neil Armstrong")

answer=input("Your answer: ").strip().lower()

#Condiional code using if and elif and else
if answer == "a" or answer == "yuri gagarin" or answer== "yuri":
   print(f"correct!, {user_name} ^_^")
   score= score + 1
elif answer == "b" or answer == "neil armstrong":
   print(f"Almost, {user_name}, but not quite.")
else:
   print(f"Wrong,{user_name}. The answer is A")


#question 2
print("\n. What is 5+3?")
answer= input("Your answer:").strip()

#Turning string into a integer
if int(answer) ==8:
   print(f"Correct, {user_name}. Your are great at maths!")
   score=score +1
else:
   print(f"Wrong,{user_name}. The answer is 8")


#Question 3 with answers
print("\n3. Which bird can fly backward?")
print("a) Blue duck")
print("b)Hummingbird")
print("c) Butterfly")
answer=input("Your answer: ").strip().lower()


if answer == "b" or answer == "hummingbird" or answer == "humming":
   print(f"Correct!, {user_name}. Great job! ")
   print("(^o^)")
   score= score + 1
elif answer == "a" or answer == "blue duck":
   print(f"Nice try,{user_name}, but blue ducks can't fly backwards")
else:
   print(f"Wrong,{user_name}.The answer is b")


#Question 4 with answers
print("\n4. What is the nation bird of New Zealand?")
print("a)kiwi")
print("b)Tui")
print("c)Ruru")
answer=input("Your answer: ").strip().lower()

if answer == "a" or answer=="kiwi" :
   print(f"Correct!,{user_name} ")
   score= score + 1
elif answer == "b" or answer == "tui":
   print(f"Good try, {user_name}, but not quite.")
else:
   print(f"Wrong,{user_name}. The answer is a")


#Question 5 with answers
print("5. Where is Mount Olympus located")
print("a)Rome")
print("b)Russia")
print("c)Greece")
answer=input("Your answer: ").strip().lower()

if answer == "c" or answer=="greece":
   print(f"Correct!, {user_name} ")
   score= score + 1
elif answer == "a" or answer == "rome":
   print(f"Close, but not correct, {user_name}.")
else:
   print(f"Wrong,{user_name}. The answer is c.")


#Question 6 with answers
print("6. What does adult cows drink?")
print("a)Water")
print("b)Milk")
print("c)Tea")
answer=input("Your answer: ").strip().lower()
if answer == "a" or answer == "water":
   print(f"Correct!, {user_name}")
   score= score + 1
elif answer == "b" or answer == "milk":
   print(f"Tricky question, {user_name}. Baby cows drink milk, not adult cows ")
else:
   print("You must choose a,b or c. Try again" )

#Question 7 with answers
print("7. What is 128+22-5")
print("a)117")
print("b)35")
print("c)145")
answer=input("Your answer: ").strip().lower()
if answer == "c" or answer== "145":
   print(f"correct!, {user_name}. Good Job. ")
   print(" (.^.)")
   score= score + 1
elif answer == "a" or answer == "117":
   print(f"Close, but not the correct answer, {user_name}.")
else:
   print(f"Wrong, {user_name} The answer is c.")

#Question 8 with answers
print("\n8.What is the diffrence between object mode and edit mode in blender?")
print("a)Object mode is for animating and edit mode is for texturing")
print("b)Object mode is for modelling and edit mode is for moving objects around ")
print("c)Object mode is for position, rotate and scale the objects while edit mode is for change their geoetry. ")
answer=input("Your answer: ").strip().lower()
if answer == "c" or answer == "geometry" in answer:
   print(f"Correct!, {user_name}")
   score= score + 1
elif answer == "b":
   print(f"Not quite,{user_name}.")
else:
   print(f"Wrong, {user_name}.The correct answer is c")

#Question 9 with answers
print("\n9.Which one is the largest planet?")
print("a)Saturn")
print("b)Jupiter")
print("c)Sun")
answer=input("Your answer: ").strip().lower()
if answer == "b" or answer == "jupiter":
   print(f"Correct!, {user_name}.")
   score= score + 1
elif answer == "a":
   print(f"Saturn is ne of the big planet, but not the biggest, {user_name}")
else:
   print(f"Wrong, {user_name}. The correct answer is b")

#Question 10 with answers
print("10. What is the largest organ in the human body?")
print("a)Skin")
print("b)Heart")
print("c)Lungs")
answer=input("Your answer: ").strip().lower()
if answer == "a" or answer == "skin":
   print('Correct!')
   print(r"\^o^/")
   score= score + 1
elif answer == "b":
   print(f"Heart is important, but not the largest orgen,{user_name}")
else:
   print(f"Wrong,{user_name}. The answer is a")

#Question 11 with answers
print("11.What is the smallest unit of matter")
print("a)Molecule")
print("b)Atom")
print("c)Proton")
answer=input("Your answer: ").strip().lower()
if answer == "b" or answer== "atom":
   print(f"Correct!,{user_name}  (o_^)")
   score= score + 1
elif answer == "a":
   print(f"Close, but molecules are made of atoms, {user_name}.")
else:
   print(f"Wrong,{user_name}. The answer is b.")

# Final Scoring
print(f"\n{user_name}, you got, {score} correct out of {TOTAL_QUESTIONS}!")

#Logical operator
if score>=8 and score <=11:
   print("Excellent work! You are amazing.")
elif score>= 5 and score<8 :
   print("Good Job! Keep improving.")
else:
   print("Don't worry. You can try again!")

# Ending with my cute ASCII art

print("\nBefore you go,here is something for you, ")                             
print(r"( \---/ )")
print(r" ) . . (  ")
print(r"(___Y___)_,--._______________________ GOOD JOB")
print(r"               `--'           `--'")

print("\nThanks for playing my quiz!!")