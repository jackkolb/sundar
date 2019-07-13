import time
import os

# LOOP: checks if the flashdrive in plugged in, if so, change the output destination to the flashdrive
def manage_output_location():
    currently_outputting_to_flashdrive = False
    while True:
        if get_flashdrive_setting and os.path.exists("/media/pi/SUNDAR_RESEARCH"):
            if not currently_outputting_to_flashdrive:
                with open("flags/destination", "w") as output_location_flag:
                    output_location_flag.write("/media/pi/SUNDAR_RESEARCH/data/")
                currently_outputting_to_flashdrive = True
        else:
            if currently_outputting_to_flashdrive:
                with open("flags/destination", "w") as output_location_flag:
                    output_location_flag.write("data/")
                currently_outputting_to_flashdrive = False
        time.sleep(1)

def get_flashdrive_setting():
    with open("settings/flashdrive", "r") as flashdrive_file:
        value = flashdrive_file.read()
    if value == "true":
        return True
    return False

# retrieves the string in the destination flag file
def get_output_location():
    destination = "none"
    with open("flags/destination", "r") as output_location_flag:
        destination = output_location_flag.readline()
    if destination == "":
        destination = "none"
    return destination