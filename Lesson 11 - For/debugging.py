
banned_items = ["slingshot","laser"]
#Create a list of invetory items
inventory = ["apple","slingshot","book","laser"]
confiscated=[]

print(f"Scanning inventory: (inventory)")


#Use while loop and with length. 
i=0 
while i<len(inventory):
    item=inventory[i]
    if item in banned_items:
        print(f"Alert! Found banned item: {inventory[0]}")
        confiscated.append(item)
        inventory.pop(i)
    else:
        i+=1

print(f"Scan complete. Total flag matches: {len(banned_items)}")

if len(confiscated)>0:
    print("Items confiscated.")

    #For number of items that confiscated  list
    for i in range(len(confiscated)):
    #Print the item listed with a number
       print(f"{i + 1}. {confiscated[i].capitalize()}")

print("Remaining intenvory:{inventory}")
       
       
           




    