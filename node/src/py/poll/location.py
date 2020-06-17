# location.py: contains a thread function for determining where to store data (flashdrive or onboard)

import time  # used to set up a time delay
import os  # used for checking if a path exists

# manage_output_location: continuously checks if the flashdrive in plugged in, if so, change the output destination to the flashdrive
def manage_output_location():
    # check if currently outputting to flashdrive
    currently_outputting_to_flashdrive = False
    with open("flags/destination", "r") as destination_file:
        if destination_file.read != "data/":
            currently_outputting_to_flashdrive = True
    
    # thread's main loop
    while True:
        # check if a flashdrive is plugged in and whether the node is set to write to a flashdrive
        # NOTE: this requires naming the flashdrive "SUNDAR_RESEARCH"
        if get_flashdrive_setting() and os.path.exists("/media/pi/SUNDAR_RESEARCH"):
            if not currently_outputting_to_flashdrive:
                with open("flags/destination", "w") as output_location_flag:
                    output_location_flag.write("/media/pi/SUNDAR_RESEARCH/data/")
                currently_outputting_to_flashdrive = True
        # otherwise, write to the onboard location (data/)
        else:
            if currently_outputting_to_flashdrive:
                with open("flags/destination", "w") as output_location_flag:
                    output_location_flag.write("data/")
                currently_outputting_to_flashdrive = False
        time.sleep(1)


# get_flashdrive_setting: checks the flashdrive setting file to see whether the node should write to a flashdrive
def get_flashdrive_setting():
    with open("settings/flashdrive", "r") as flashdrive_file:
        value = flashdrive_file.read()
    if value == "true":
        return True
    return False


# get_output_location: retrieves the string in the destination flag file
def get_output_location():
    destination = "none"
    with open("flags/destination", "r") as output_location_flag:
        destination = output_location_flag.readline()
    if destination == "":
        destination = "none"
    return destination
