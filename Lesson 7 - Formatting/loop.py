#Game 1
#infinite loop
# name=input("Enter your name")
# while name == "":
#     print("You did not enter your name")
#     print(f" Hello{name}")

#So make it correct by making the user toescape from infinite loop
# name=input("Enter your name:")
# while name == "":
#     print("You did not enter your name")
#     name=input("Enter your name:")
# print(f"Hello {name}")

#Game 2
# age=int(input("Enetr your age"))
# while age <0:
#     print("Age can't be 0") 
#     age=int(input("Enter your age"))
# print(f"You are {age} years old")


#Game 3
# food=input("Enter a food you like (q to quit): ")
# while not food == "q":
#     print(f"You like {food}")
#     food=input("Enter another food you like (please enter stop to quit): ")
# print("bye")


#Use of "for" loops
# for x in range(1,11):
#     print(x)

#counting backwards
# for x in reversed (range(1,11)):
#     print(x)
# print("Yayyyyyyy")

#counting from 2s
for x in range(1,11,3):
    print(x)