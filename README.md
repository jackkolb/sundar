# Sundar's Lab
Our Codebase for Sundar's Lab

## Overview:

There are several modules that work together.

To start the program, run run.sh.

### run.sh

run.sh simply runs loader.py.

### loader.py

loader.py runs the Main Module (main.py), restarting it if it stops.

### Main Module (main.py)

The Main Module starts the GitHub Check Module, loads the settings file, starts the LCD Module, and lastly runs the Collection Module on an infinite loop.

### GitHub Check Module (gitcheck.py)

The GitHub Check Module repeatedly runs "git pull" to keep the codebase updated. If the codebase is updated, this module will set a file (settings/git_flag) contents to "RESET". The Main Module will see this change and reset itself.

### LCD Module (lcd.py)

The LCD Module controls a 16x2 LCD display. It gets the device's IP address and currently connected WiFi network, reads the (settings/out_file) to get the name/location of the data output file, and gets the remaining disk storage. This information is displayed on the screen.

### Collection Module (main.c -> collect.o)

The Collection Module is a compiled C script that collects data from the accelerometer and stores it to a given file:
`	collect.o PREFERRED_OUTPUT_DIRECTORY PREFERRED_OUTPUT_FILE SECONDARY_OUTPUT_FILE`

