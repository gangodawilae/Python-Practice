# =====================================================================
#  TASK: Change the code below to use cleaner print formatting
# =====================================================================

# User input
username = input("Enter friend's name: ").strip().upper()
messages_count = int(input("Number of unread text messages: "))
is_online = input("Are they online right now? (yes/no): ").strip().lower() == "yes"

# Output current status
print = (f"💬  [{username}] + is typing a response...") 


# Output message log
print=(f"✉️ You have  [{messages_count}]  + unread messages waiting from + [{username}].")


# Output friend list status
print = (f"👤 USER: "  {username} " \n ONLINE STATUS: " + {is_online} + " \n SYNC COMPLETE.")
