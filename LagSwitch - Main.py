# LagSwitch
# Script made by @Hermivore
print("Loading")
import os
import sys
import keyboard
import time
from win10toast import ToastNotifier
import threading
print("Loaded")

sys.stderr = open(os.devnull, 'w') # Write errors to nowhere

# Subroutines

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Notif System
def notif_main(title, message, duration=2): # try and except because the notif system is prone to crashing
    try:
        toaster = ToastNotifier()
        toaster.show_toast(title, message, icon_path="", duration=duration)
    except:
        time.sleep(2.2)
        notif(title, message, duration=2)
        

# Subroutine to be called
def notif(title, message, duration=2):
    thread = threading.Thread(target=notif_main, args=(title, message, duration))
    thread.start()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
# Internet subroutines
def enable_internet_main():
    global network_action, mode, amount
    while True:
        if not network_action:
            # amount += 1 # Dont ahve to worry about enable subroutines, as they not harmful
            network_action = True
            os.system("ipconfig /renew"); os.system("cls")
            notif("LagSwitch", "Switch Disabled - Internet Enabled")
            print(f"Switch Disabled - Internet Enabled \n{mode} in use")
            network_action = False
            # amount -= 1
            break

def disable_internet_main():
    global network_action, mode, amount
    while True:
        if not network_action:
            if amount > 1:
                break # Exit active disable subroutines, otherwise we end up disabling the internet for good lol
            amount += 1
            network_action = True
            os.system("ipconfig /release"); os.system("cls")
            notif("LagSwitch", "Switch Enabled - Internet Disabled")
            print(f"Switch Enabled - Internet Disabled \n{mode} in use")
            network_action = False
            amount -= 1
            break
    

# Subroutines to be called
def enable_internet():
    thread = threading.Thread(target=enable_internet_main)
    thread.start()

def disable_internet():
    thread = threading.Thread(target=disable_internet_main)
    thread.start()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Load hotkey data
def hotkey_data():
    try: 
        file = open("hotkey.txt", "r")
        hotkey = file.readline()

    except:
        print("We dont have a hotkey data file, creating one")
        file = open("hotkey.txt", "w")
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

# Load mode data
def mode_data():
    try: 
        file = open("mode.txt", "r")
        mode = file.readline()

    except:
        print("We dont have a mode data file, creating one")
        file = open("mode.txt", "w")
        mode = (input("What mode do you want to use (1 OR 2): \n1. Toggle \n2. Hold\n")).strip()

        if mode == "1" or mode == "2":
            file.write(mode)
            file.close()

        else:
            input("Make sure you only enter 1 or 2, press enter to close the script")
            exit()

        print("Created file successfully, if you want to change the file, delete mode.cum")
        time.sleep(1)
        os.system("cls")
    return mode

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Setup
def setup():
    global hotkey, mode, network_action, amount
    # Load data
    hotkey = hotkey_data()
    mode = mode_data()
    network_action = False # False = no actions are being performed, true means actions are being performed
    amount = 0
    print("Started")
    os.system("cls")
    # Run main loop
    return hotkey, mode

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Mains

# Toggle
def main_1():
    global hotkey
    event = keyboard.read_event()
    event = event.name

    if event == hotkey: # Key pressed, enable the lagswitch
        disable_internet()

        time.sleep(0.5)

        while True:
            event = keyboard.read_event()
            event = event.name

            if event == hotkey: # Key pressed again, disable the lagswitch
                enable_internet()
                break
            time.sleep(0.1)
        time.sleep(0.5) # Delay to prevent the event from triggering again

# Hold
def main_2():
    global hotkey
    if keyboard.is_pressed(hotkey):
        disable_internet()

        # Hold the program while pressed
        while keyboard.is_pressed(hotkey):
            time.sleep(0.1) # Stop the script from lagging the keyboard with a small delay
            pass

        # Notify
        enable_internet() # Key has been released, re-enable internet
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def main_main(): # the main main 🗣
    global mode
    try:
        if mode == "1":
            mode = "Toggle"
            print(f"Switch Disabled - Internet Enabled \n{mode} in use")
            while True:
                time.sleep(0.1) # Stop the script from lagging the keyboard with a small delay
                main_1() # Toggle
        else:
            mode = "Hold"
            print(f"Switch Disabled - Internet Enabled \n{mode} in use")
            while True:
                time.sleep(0.1) # Stop the script from lagging the keyboard with a small delay (i restarted my pc 3 times before figuring out this was the problem)
                main_2() # Hold
    except Exception as e:
        print(e)
        print()
        input("A fatal error happened, press enter to continue, or close the program. The error has been printed above.")
        main_main()
        # this is a bad idea, but the notif system is a tad unstable ;3

hotkey, mode = setup()

main_main()
