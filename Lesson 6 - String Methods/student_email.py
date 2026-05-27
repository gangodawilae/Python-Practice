# Create a student email creator that uses first and lat name plus id
# eg. smithjohn123@fake.school.nz

# Get input (first, last, id) and save in variables
first_name=input("Please enter your first name")
last_name=input("Please enter your last name")
student_id=input("Please enter your student ID")


# Strip input to remove accidental spaces and turn names into lowercase (resave in variables)
first_clean = first_name.strip().lower()
last_clean = last_name.strip().lower()
id_clean = student_id.strip().lower()


# {last_clean}

# Output the final email address

print("Your generated email is:",last_clean + first_clean + id_clean + "@fake.school.nz") 
# --------------------------------

# EXTENSION
# Create a temporary password to output as well
# print("Create a temporay password here")
print("Temporray passord details")

# It should be their names in all uppercase and their id divided by 10
temporary_first_upper = first_clean.upper()
temporary_last_upper = last_clean.upper()
 #Divide by 10
divided_id = int(id_clean)//10

#Use all for the final password
temporary_password=temporary_first_upper+ temporary_last_upper + str(divided_id)


#The final password
print("Your temporary password is:", temporary_password)

# --------------------------------

# EXPERT
# Create a WSCW email creator
# Get the users first and last name, then randomly generate an ID number (8 digits long)
# Output the email addess (lastf.wsc.school.nz) 
# - you'll need to strip down the first name to just first letter
# Output their id number
# Output a temporary password (all uppercase). You can choose how you create this, 
# but it needs to be unique for each user


