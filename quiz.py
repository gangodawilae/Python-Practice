#This function ask one question. It shows the question and options, and cleans the user's input properly.
#And this makes them retry if they type nothing, and returns whather they were corrent. 
def ask_question(question, options, correct_answers):
   print("\n" + question)


   #Print options if the question has any
   for option in options:
      print(option)

   #Ask the user for an answer in this loop until they type something correct
   while True:
      answer = input("Your answer:\n").strip().lower()
      if answer == "":
         print("Please type something, so I can check your answer.")
         continue
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
      print("Excellent work! You are amazing. (\\^o^/)")
      print("*********************************")
   elif score>= 5:
      print("Good Job! Keep improving.(^o^)")
      print("*********************************")
   else:
      print("Don't worry. You can try again!(o_^)")
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
   print(f"Welcome to my quiz game! {name}")
   print("\nINSTRUCTIONS:Choose the correct option,(a, b, or c) or write the answer")
   input("Are you ready...? Press yes to start")
   print(f"\nLet's start!!, I believe in you, {name}!")
   print("(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)(^.^)")


   #This is the list of questions, and each question is lsted as question, list of options, list of orrect answer.
   questions = [
      "1. Who is the first person to go to space?", 
      "2. What is 5+3?",
      "3. Which bird can fly beackward?",
      "4. What is the national bird of New Zealand?",
      "5. Where is Mount Olympus located?",
      "6. What do adult cows drink?",
      "7. Whatis 128+22-5?",
      "8. What is the difference between edit mode and object mode in Blender?",
      "9. Which is the largest planet?",
      "10. What is the largest organ in human body?",
      "11. What is the smallest unit of matter?",
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


   #Integer score starts with 0
   score=0


   #This loop goesthrough every question one by one using its index number.
   for i in range (len(questions)):

      #This function do two things. is_correct = true or fase depend on what user put. And seecond is, correct answers = the correct answer text to show if they get it wrong.
      is_correct, correct_answer = ask_question(
         questions[i],
         options[i],
         correct_answers[i]
      )

      #Give feedback like they got it correct or wrong after each question.
      if is_correct:
         print(f"\nCorrect, {name}!. Great Job!!!^_^")
         print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
         score+=1

      else:
         print(f"\nWrong, {name}. The correct answer is {correct_answer}. Try again next time.")
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
