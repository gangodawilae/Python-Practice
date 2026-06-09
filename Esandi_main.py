# # print("hello")
# # print()
# # print("hello")
# # print("I'm coding")
# # print("I'm coding")

# # input("Name?")
# # print("Hello")

# # input("Name?\n")
# # print("Name?")
# # input()

# # input("School?\n")
# # print("School")
# # input()

# print(5-5)
# print("5" + "5")
# print(5.0 / 5.0)
# print("5" + 5)
# print(5+ 5.0)

# name = "Helen"
# print("My name is" + name)

# name = "Helen"
# print("My name is", name)

# name="Helen"
# age = 15
# print(name + " is " + age)

# name = "Helen"
# age = 15
# print(name, "is", age)

# age = 5
# print("He is " + age)

# age = 5
# print("He is " + str(age))

# age = input("Age?")
# print("Birth year:", 2026 - age)
# age = input("Age?")
# print("Birth year:", 2026 - int(age))
# MULT_NUM=5
# INSTRUCTIONS ="Choose a number and I will muliply it by" +str(MULT_NUM)
# name=input("Hi, there! What's your name?")
# print("Hi", name)
# print(INSTRUCTIONS)
# num=input("What number should I multiply?")
# print("The anwer is:", int(num)*MULT_NUM)
# print(5+5==10)
# print(5+5==8)
# print (5== 5.0)
# print("hello"=='hi')
# print(5+5>=10)
# print(5+5 >=8)
# print(5 !=5)
# print( 5 !=6)
# if 5 < 10:
# if 5 < 10:
# print('hello')

# if 5<10:
#     print('hello')
# if 5 < 10:
#     pass
# if 10 != 10:
#     print('hello')
# print('goodbye')

# if 5 < 10:
# print('Less than 10')
# print('10 or more')

# if 5 < 10:
# print('Less than 10')
# else:
# 	print('10 or more')

# name = input()
# if name == "Athena":
#     print("Goddess of wisdom")

# if name == "Apollo":
#     print("God of the sun")
# print('hello'.upper())
# print('HELLO'.lower())
# # if 'HELLO' == 'hello':
# # print('The same!')
# if 'HELLO'.lower() == 'hello':
#     print('The same!')
# age = 10
# if age == 11 or 12:
#     print('Access granted')
# age = 10
# if age == 11 or age == 12:
#     print('Access granted')

# f“Hello {name}.”
# name = 'Paul'
# age = 15
# print(name + ' is ' + age)

# name = 'Paul'
# age = 15
# print(name + ' is ' + age)

# name = 'Paul'
# age = 15
# print(name + ' is ' + age)

# name = 'Paul'
# age = 15
# print(f'{name} is {age}')


# guess = input('What’s the password?')
# print('Checking password is a match…')
# while guess != 'secret':
#     guess = input('Try again')
# print('Checking password is a match…')
# input('Welcome!')

# print(random.random())

# import random
# print(random())

# import random
# print(random.random())
# print(random.randint(0,10))
# random.randint(1, 10)

# count = 0
# while count < 5:
#     print("Hello!")
#     count = count + 1

# timer = 3
# while timer > 0:
#     print("Counting down!")
#     timer = timer - 1

# user_input = ""
# while user_input != "exit":
#     user_input = input()

# user_input = 'idk'
# try:
#     num = int(user_input)
#     print(f'You picked {num}')
# except:
# 	print(f'{user_input} is not a number!')

# count = 0
# while count < 10:
#     print('Counting…')
#     if count < 5:
# 	    break
#     print('Almost done…')
# print('Finished!')


# count = 0
# while count < 10:
#     print('Counting…')
#     if count < 5:
# 	    continue
#     print('Almost done…')
# print('Finished!')

# while True:
# 	guess = input('Guess a country')
# if guess.lower().strip() == 'malawi':
# 	break
# print('Try again.')
# print('Well done!')

# ["apple", "ornages", "5", "True", "5.0"]

# animals= ["cat", "dog", "bird"]
# print(animals[0])
# print(animals[1])
# print(animals[2])


# questions = ["What is 2+2?", "What is the capital of NZ?", "What colour is the sky?"]

# for q in questions:
#     print(q)
    
# numbers= [1,2,3]
# numbers.append(4)
# print(numbers)

# shopping_list = ['apples','plums','pizza']
# print(shopping_list[2])

# shopping_list = ['apples','plums','pizza']
# print(shopping_list[3])

import random
shopping_list = ['apples','plums','pizza']
print(shopping_list[random.randint(0,2)])