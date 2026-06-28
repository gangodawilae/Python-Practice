#Shuffling questions
import random


#These color codes print the text in diffrent colors. Like green for correct.Red for wrong. Orange for hints. 
GREEN="92"
RED="91"
ORANGE="93"

#This adds color to any text we wants.
def color(text,code):
   return f"\033[{code}m{text}\033[0m"


#This function ask one question. It shows the question and options, and cleans the user's input properly.
#And this makes them retry if they type nothing, and returns whather they were corrent. 
def ask_question(question, options, correct_answers,hint_in_text):

   #Put a border
   print("\n+" + "-" * 60 +"+\n")

   #Print the questions
   print( question)


   #Print options if the question has any
   for option in options:
      print(option)

   #The keep the track wheather the user used their hint
   hint_used=False

   #Ask the user for an answer in this loop until they type something correct
   while True:
      answer = input("Your answer (or type hint for a hint):\n").strip().lower()
      if answer == "":
         print(color("Please type something, so I can check your answer.",ORANGE))
         continue
      
      #If the user ask for a hint
      if answer == "hint":
         if not hint_used:
            print(color("Hint:"+ hint_in_text, ORANGE))
            hint_used=True
         
         else:
            print(color("You already used your hint for this question",RED))
         continue
         #If the user type a real, and proper answer, break the loop
      break

   #Check if the user's answer matches any correct answer.
   is_correct= answer in correct_answers
   #Return correctness and the correct answer.
   return is_correct,correct_answers[0]



   #This function prints the final results of the quiz.
   #Like if shows the user's score, gives feedback based on their score.
def show_results(name, score, total):

   print("\n******************************")

   print("RESULTS")
   
   print(f"\n{name}, you got, {score} correct out of {total}!")

   print("\n>----(^_^)----<")

   #This is the part where, feedbacks gives on their score.
   if score>=8:
      print("Excellent work! You are amazing. (\\^o^/)",GREEN)
      print("*********************************")
   elif score>= 5:
      print("Good Job! Keep improving.(^o^)",ORANGE)
      print("*********************************")
   else:
      print("Don't worry. You can try again!(o_^)",RED)
      print("*********************************")

   

   # Ending with my cute ASCII art

   print("\nBefore you go,here is something for you, ")                             
   print(r"( \---/ )")
   print(r" ) . . (  ")
   print(r"(___Y___)_,--._______________________ GOOD JOB")
   print(r"               `--'           `--'")

   
   print("(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)")

#Main program
def play_quiz():
   
   #Ask for users's name, remove extra space and write it nicely
   name=input("Hello! What is your name?").strip().title()

   #Start of the quiz with a welcome message to my quiz
   print(color(f"Welcome to my quiz game! {name}",ORANGE))
   print("\nINSTRUCTIONS:Choose the correct option,(a, b, or c) or write the answer")
   input("Are you ready...? Press yes to start")
   print(f"\nLet's start!!, I believe in you, {name}!")
   print("(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)")


   #This is the list of questions, and each question is lsted as question, list of options, list of orrect answer.
   questions = [
      " Who is the first person to go to space?", 
      " What is 5+3?",
      " Which bird can fly beackward?",
      " What is the national bird of New Zealand?",
      " Where is Mount Olympus located?",
      " What do adult cows drink?",
      " Whatis 128+22-5?",
      " What is the difference between edit mode and object mode in Blender?",
      " Which is the largest planet?",
      " What is the largest organ in human body?",
      " What is the smallest unit of matter?",
   ]

   options = [
      ["a) Yuri Gagarin", "b) Thomas Edison", "c) Neil Armstrong"],
      [],
      ["a) Blue duck", "b) Hummingbird", "c) Butterfly"],
      ["a)Kiwi", "b)Tui","c)Ruru"],
      ["a)Rome", "b)Russia", "c)Greece"],
      ["a)Water","b)Milk", "c)Tea"],
      ["a)117", "b)35", "c)145"],
      ["a) Object mode is for animating and edit mode is for texturing", "b) Object mode is for modelling and edit mode is for moving objects around", "c) Object mode is for position, rotate and scale the objects while edit mode is for change their geometry."],
      ["a) Saturn", "b) Jupiter", "c) Sun"],
      ["a) Skin", "b) Heart", "c) Lungs"],
      ["a)Molecule", "b)Atom", "c)Proton"]
   ]


   correct_answers=[
      ["a", "yuri", "yuri gagarin"],
      ["8", "Eight", "eight"],
      ["b", "hummingbird", "humming"],
      ["a", "kiwi"],
      ["c", "greece"],
      ["a", "water"],
      ["c", "145"],
      ["c", "geometry"],
      ["b", "jupiter"],
      ["a", "skin"],
      ["b", "atom"]
   ]

   hints=[
      "He is a Russian cosmonaut. First name is Yuri!",
      "It is a number more than 7 and less than 9.",
      "It is a very tiny bird",
      "It can't fly",
      "It is in Greece",
      "They drink water, not milk",
      "Do the addition first",
      "Edit mode changes the shape of the object",
      "It massive than 1,300 Eartsh could fit inside it.",
      "It covers your whole body",
      "It is smaller than a molecule"
   ]

   #Create a list of index
   #This lets us shuffle the order of the question
   indexes = list(range(len(questions)))

   #Shuffle the indexes so the questions show in diffrent order.
   random.shuffle(indexes) 

   #Integer score starts with 0
   score=0


   #This loop goesthrough every question one by one using its index number.
   for i in indexes:

      #This function do two things. is_correct = true or fase depend on what user put. And seecond is, correct answers = the correct answer text to show if they get it wrong.
      is_correct, correct_answer = ask_question(
         questions[i],
         options[i],
         correct_answers[i],
         hints[i]
      )

      #Give feedback like they got it correct or wrong after each question.
      if is_correct:
         print(color(f"\nCorrect, {name}!. Great Job!!!^_^",GREEN))
         print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
         score+=1

      else:
         print(color(f"\nWrong, {name}. The correct answer is {correct_answer}. Try again next time.",RED))
         print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

   
   #Show the final results.
   show_results(name,score, len(questions))


#Replay the loop
while True:
   play_quiz()
   

   again= input("\n Do you want to play again? (yes/no): ").strip().lower()
   if again not in ("yes", "y"):
      print("\nThanks for playing my quiz!!")
      print("Goodbye.....")
      print(".oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo. ")

      break
