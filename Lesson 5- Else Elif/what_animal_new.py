print("Welcome to the animal quiz")
score=0
#First ask two questions aout themsevles
question1 = input("Do you prefer being,\n1) indoors \n2) outdoors?")
question2 = input("Are you more, \n1)quiter \n2)louder")

#If they choosed the 1st option, ask questions
if question1== "1":
    print("You choosed indoors. Please answer these questions")

    answer_1=input("Do you like warm places\n 1)yes 2)no")
    if answer_1 =="1":
        score+= 1
    answer_2=input("Do you enjoy relaxing? \n1)yes 2)no")
    if answer_2== "1":
        score+= 1
    answer_3=input("Do you like small spaces? \n1)yes 2)no")
    if answer_3 == "1":
        score+= 1
    answer_4 = input("Do you like being alone? \n1)yes 2)no")
    if answer_4 == "1":
        score+= 1
    answer_5= input("Are you active at night? \n1)yes 2)no")
    if answer_5 == "1":
        score+= 1
elif question1 =="2":
    print("You choosed outdoors! Please answer these questions")

    answer_1 = input("Do you like running?\n1)yes 2)no")
    if answer_1=="1":
        score+= 1
    answer_2 = input("Do you like climbing? \n1)yes 2)no")
    if answer_2 =="1":
        score+= 1
    answer_3= input("Do you like being around people? \n1)yes 2)no")
    if answer_3 =="1":
        score+= 1
    answer_4 = input("Do you like exploring? \n1)yes 2)no")
    if answer_4 =="1":
        score+= 1
    answer_5= input("Are you energetic?  \n1)yes  2)no")
    if answer_5 =="1":
        score+= 1
# else:
#     print("Please answer the questions")
#Check whether which animal
print("Wait, now I'm figuring out your animal")
if score<=2:
    print("You are a cat")
elif score==3:
    print("You are a fox")
elif score==4:
    print("You are a dog")
else:
    print("You are a wolf")