import random

#keep the maximun attempts in a constant
MAX_ATTEMPTS = 3

#Counte for how many attemps have been made and keep in a variable
attempts = 0
system_status = "OFFLINE"

#Keep looping while the system is offline and tries are less than 3
while attempts < MAX_ATTEMPTS and system_status == "OFFLINE":
    boot_code = input("Enter boot code (START): ")

#If user type start correctly in any case 
    if boot_code.upper().strip() == "START":
        print("System booting...")
#Change system to online
        system_status = "ONLINE"
    else:
        print("Invalid boot code.")
#Add one to number of tries
        attempts += 1

        rand_num = random.randint(1,10)
        if rand_num == 5:
            print("Something went wrong")

#After the loop ends, show what happened
if system_status == "ONLINE":
    print("System is online.")
else:
    print("System failed to boot after", MAX_ATTEMPTS, "attempts.")



# TODO Add a 'magic eight ball' program for once the system is booted
# TODO Get the user to ask a yes/no question
# TODO Randomise a number and use that number to give them a response