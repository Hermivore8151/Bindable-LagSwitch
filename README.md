# Bindable-LagSwitch
A simple Lag Switch designed for windows, with a toast notification when enabled / disabled, and hotkey support

# Hotkey Creation + Downloading
- - Download the exe, or the .py file if you want to make any changes to the original script
- - On first run, it will ask you to create a keybind, it can be any single key
- - It will also ask for the mode to use if you are using the exe, the .py file is not up to date
- - It will then store this file under hotkey.cum and mode.cum respectivly, delete these file to reset them

# Script Usage
- - To enable, press your assigned hotkey
- - To disable, press your assigned hotkey again
  - OR
- - When using hold, hold to enable, release to disable

# How it works
It uses the os import to run a simple command:
- ipconfig /release (To disable the connection)
- ipconfig /renew (To Re-Enable the connection)

# Other
- Credits to https://github.com/Alexplayrus1 and https://github.com/dannws for finding the method used
- DM me on Discord (@hermivore) for support and any issues
