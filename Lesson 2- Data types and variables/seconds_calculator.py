# Create a calculator that asks the user for a number (of days)
# and outputs how many seconds in that number of days

# Values - start by writing constants to hold:
# The number of seconds in a minute
SECONDS_IN_MINUTE=60
# The number of minutes in an hour
MINUTES_IN_HOUR=60
# The number of hours in a day
HOURS_IN_DAY=24

# Get input from the user and save it in a variable
days = int(input("Enter number of days:"))
# Change the value into an integer and resave in the variable


# Calculate the number of seconds using * with the input and your constants. 
total_seconds= days* HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE
# Save it in a new variable.

# Output the answer
print("There are", total_seconds, "seconds in", days, "days.")
# ---------------------------------

# EXTENSION 1
# Also output how many total hours and how many total minutes in the days

# ---------------------------------
# EXTENSION 2
# Create another calculator that does the opposite (input is seconds, output is days)

# ---------------------------------

# EXPERT (for those who already know some Python)
# Create the calculator above, but...
#   allow your user to choose the input and output type (seconds, minutes, hours, days)
#   Loop the calculator so they can do it again with having to reopen the program.