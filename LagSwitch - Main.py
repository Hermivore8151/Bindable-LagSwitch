# LagSwitch
# Script made by @Hermivore
print("Loading")
import os
import keyboard
import time
from win10toast import ToastNotifier
print("Loaded")

# Notif System
def notif(title, message, duration=2):
    try:
        toaster = ToastNotifier()
        toaster.show_toast(title, message, icon_path="", duration=duration)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Load save data
def hotkey_data():
    try: 
        file = open("hotkey.cum", "r")
        hotkey = file.readline()

    except:
        print("We dont have a hotkey data file, creating one")
        file = open("hotkey.cum", "w")
        print("Press the key you want to use as a bind...")
        event = keyboard.read_event()
        event = event.name
        hotkey = event

        print(f"Read hotkey as {hotkey}")
        file.write(event)
        file.close()
        print("Created file successfully, if you want to change the file, delete hotkey.cum")
        time.sleep(1)
        os.system("cls")
    return hotkey

# Main
def main():
    global hotkey
    event = keyboard.read_event()
    event = event.name

    if event == hotkey: # Key pressed, enable the lagswitch
        # Enable
        os.system("ipconfig /release")
        os.system("cls")
        # Alert
        notif("LagSwitch", "Switch Enabled - Internet Disabled"); os.system("cls")
        print("Switch Enabled - Internet Disabled")
        time.sleep(0.5)

        event = keyboard.read_event()
        event = event.name

        if event == hotkey: # Key pressed again, disable the lagswitch
            # Disable
            os.system("ipconfig /renew")
            os.system("cls")
            # Alert
            notif("LagSwitch", "Switch Disabled - Internet Enabled"); os.system("cls")
            print("Switch Disabled - Internet Enabled")

# Load data
print("Started")
hotkey = hotkey_data()

# Run main loop
while True:
    main()
    time.sleep(0.5)