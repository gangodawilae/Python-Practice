# =====================================================================
#  TASK: Change the code below to use cleaner print formatting
# =====================================================================

# User input
username = input("Enter friend's name: ").strip().upper()
messages_input = input("Number of unread text messages: ").strip()
if messages_input.isdigit():
    messages_count=int(messages_input)
else:
    print("please enter a correct number")
is_online = input("Are they online right now? (yes/no): ").strip().lower() == "yes"

# Output current status
status_message= f"💬  [{username}]  is typing a response..."
print(status_message)

# Output message log
preview_message=f"✉️ You have  {messages_count}  unread messages waiting from  [{username}]."
print(preview_message)

# Output friend list status
friend_message = f"👤 USER: {username}  \n ONLINE STATUS: {is_online} \n SYNC COMPLETE."
print(friend_message)