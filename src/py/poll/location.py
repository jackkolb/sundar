import time
import os

def set_output_location():
    currently_outputting_to_flashdrive = False
    while True:
        if os.path.exists("/media/pi/SUNDAR_RESEARCH"):
            if not currently_outputting_to_flashdrive:
                with open("flags/destination", "w") as output_location_flag:
                    output_location_flag.write("/media/pi/SUNDAR_RESEARCH/data/raw_data.txt")
                currently_outputting_to_flashdrive = True
        else:
            if currently_outputting_to_flashdrive:
                with open("flags/destination", "w") as output_location_flag:
                    output_location_flag.write("data/raw_data.txt")
                currently_outputting_to_flashdrive = False
        time.sleep(1)


def get_output_location():
    destination = "none"
    with open("flags/destination", "r") as output_location_flag:
        destination = output_location_flag.readline()
    return destination