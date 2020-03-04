# Sundar's Lab
Our Codebase for Sundar's Lab project

## Overview:

There are several modules that work together. This ReadMe works best describing what the individual modules do and how they interact.

To start the program, run ./run.sh.

### run.sh

run.sh simply runs the Loader Module (loader.py).

### Loader Module

The Loader Module is the base system bootstrap: it runs the Main Module (main.py), restarting the Main Module it if it stops.

### Main Module (py/main.py)

The Main Module starts the main submodules and runs the Collection module on an infinite loop, checking for control and git updates after each collection.

### GitHub Check Module (py/poll/gitcheck.py)

The GitHub Check Module repeatedly runs "git pull" to keep the codebase updated. If the codebase is updated, this module will set a file (flags/git_flag) contents to "RESET". The Main Module will see this change and reset itself.

### LCD Module (py/poll/lcd.py)

The LCD Module controls a 16x2 LCD display. It gets the device's IP address and currently connected WiFi network, reads the (settings/out_file) to get the name/location of the data output file, and gets the remaining disk storage. This information is displayed on the screen.

### LED Module (py/poll/led.py)

The LED Module controls an RGB LED: it periodically reads from a flag file (flags/damage) and displays a green/yellow/red light according to the current damage level.

### Collection Module (c/main.c -> collect.o)

The Collection Module is a compiled C program that collects data from the accelerometer and stores it to a given file:
`	collect.o PREFERRED_OUTPUT_DIRECTORY PREFERRED_OUTPUT_FILE SECONDARY_OUTPUT_FILE`

### Webserver Module (www/node/
