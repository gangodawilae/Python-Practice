print("--- Daily Step Tracker ---")
steps_int = int(input("How many steps did you walk today? "))

#This is the goal
DAILY_GOAL = 5000
#Now debug these word problems
if steps_int == 0:
    print("Did you forget your phone today? You have 0 steps!")
elif steps_int == DAILY_GOAL:
    print("Bullseye!, You hit your goal today!")
elif steps_int >= 10000:
    print("Amazing! You walked over 10,000 steps! You are a Pro Athlete.")
elif steps_int >= 5000:
    print("Good start, but try to walk a bit more tomorrow!")
else:
    print("Keep moving! Every step counts.")
print("Tracker closing...")
