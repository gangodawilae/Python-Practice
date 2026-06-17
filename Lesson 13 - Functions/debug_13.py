#Save the secutiry_statues and alram sound in a variable
security_status = "LOCKED"
alarm_sound = "SIREN"

def trigger_alarm():
    print(f"Alert! Sounding the {alarm_sound}")

def check_system():
    print(f"Checking home network stability...")
    if security_status == "LOCKED":
        print("All doors are secured.")
    else:
        trigger_alarm()

#New function added to funfill the requirnment.
#Define a new function called reset_system.
def reset_system():
    #Inside te function, print "system rebooting...."
    print("System is rebooting...")

def main():
    print(f"The current alarm sound is: {alarm_sound}")
    check_system
    reset_system

#Execute the main function
if __name__ == "__main__":
    main()
