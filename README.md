# Bindable-LagSwitch
A simple Lag Switch designed for windows, with a toast notification when enabled / disabled.

# How to use
- Hotkey Creation
--Download the exe, or the .py file if you want to make any changes to the original script
--On first run, it will ask you to create a keybind, it can be any single key
--It will create a file called hotkey.cum (dont ask why, its funny)
- Usage
--To use, press your assigned hotkey, and it should show a toast along with the action in console
--It is togglable, so press again to disable

# Restting the keybind
If you want to reset the keybind, just delete the hotkey file and it will ask you to create another one

# How it works
It uses the os import to run a simple command
To disable the connection:
- ipconfig /release
To Re-Enable the connection
- ipconfig /renew

# Other
Credits to https://github.com/Alexplayrus1 and https://github.com/dannws for finding the method used
dm me on discord @hermivore for support and any issues
