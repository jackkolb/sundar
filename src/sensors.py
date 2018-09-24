import time
import src.gitcheck
import src.logs
import multiprocessing
import datetime
#import src.drive

from src.accelerometer.LIS3DH import LIS3DH
import RPi.GPIO as GPIO


accelerometer_status_led_pin = 25

accelerometer_sensor = "NONE"


def initialize_accelerometer():
    try:
        global accelerometer_sensor
        accelerometer_sensor = LIS3DH(debug=True)  # will be initialized with accelerometer_initialize()
        accelerometer_sensor.setRange(LIS3DH.RANGE_2G)
        return True
    except OSError:
        src.logs.log("Failed to initialize accelerometer")
        return True

# reads data from the temperature sensor
def temperature_sensor_poll():
    return 75


# continuously polls the temperature sensor as per the specified frequency
def temperature_sensor_loop(frequency):
    while True:
        with open("data/temperature/temperature_" + src.logs.get_date() + ".data", "a") as temperature_data_file:
            temperature_reading = temperature_sensor_poll()
            timestamp = time.time()
            temperature_data_file.write(str(timestamp) + ", " + str(temperature_reading) + "\n")

        time.sleep(1.0 / float(frequency))


# reads data from the humidity sensor
def humidity_sensor_poll():
    return 83


# continuously polls the humidity sensor as per the specified frequency
def humidity_sensor_loop(frequency):
    while True:
        with open("data/humidity/humidity_" + src.logs.get_date() + ".data", "a") as humidity_data_file:
            humidity_reading = humidity_sensor_poll()
            timestamp = time.time()
            humidity_data_file.write(str(timestamp) + ", " + str(humidity_reading) + "\n")

        time.sleep(1.0 / float(frequency))



# reads data from the accelerometer
def accelerometer_sensor_poll():
    x = accelerometer_sensor.getX()
    y = accelerometer_sensor.getY()
    z = accelerometer_sensor.getZ()

    # raw values
    #print("DEBUG: X: %.6f\tY: %.6f\tZ: %.6f" % (x, y, z))
    return x, y, z


# continuously polls the accelerometer as per the specified frequency
def accelerometer_sensor_loop(frequency):
    while True:
        with open("data/accelerometer/accelerometer_" + src.logs.get_date() + ".data", "a") as accelerometer_data_file:
            GPIO.output(accelerometer_status_led_pin, GPIO.HIGH)
            accelerometer_reading_x, accelerometer_reading_y, accelerometer_reading_z = accelerometer_sensor_poll()
            GPIO.output(accelerometer_status_led_pin, GPIO.LOW)
            timestamp = time.time()
            accelerometer_data_file.write(str(timestamp) + ", [" + str(accelerometer_reading_x) + str(accelerometer_reading_y) + str(accelerometer_reading_z) + "] \n")

        time.sleep(1.0 / float(frequency))


# reads data from the current sensor
def current_sensor_poll():
    return 2


# continuously polls the current sensor as per the specified frequency
def current_sensor_loop(frequency):
    while True:
        with open("data/current/current_" + src.logs.get_date() + ".data", "a") as current_data_file:
            current_reading = accelerometer_sensor_poll()
            timestamp = time.time()
            current_data_file.write(str(timestamp) + ", " + str(current_reading) + "\n")

        time.sleep(1.0 / float(frequency))


# manages the sensor processes
def sensor_manager(settings):

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(accelerometer_status_led_pin, GPIO.OUT)
    

    # get the sensor frequencies from the settings
#    temperature_frequency = settings["TEMPERATURE_FREQUENCY"]
#    humidity_frequency = settings["HUMIDITY_FREQUENCY"]
    accelerometer_frequency = settings["ACCELEROMETER_FREQUENCY"]
#    current_sensor_frequency = settings["CURRENT_SENSOR_FREQUENCY"]

    # create the sensor processes
#    src.logs.log("[SENSORS] Starting Temperature Process")
#    temperature_process = multiprocessing.Process(target=temperature_sensor_loop, args=(temperature_frequency,))
#    src.logs.log("[SENSORS] Starting Humidity Process")
#    humidity_process = multiprocessing.Process(target=humidity_sensor_loop, args=(humidity_frequency,))
    src.logs.log("[SENSORS] Starting Accelerometer Process")
    accelerometer_process = multiprocessing.Process(target=accelerometer_sensor_loop, args=(accelerometer_frequency,))
#    src.logs.log("[SENSORS] Starting Current Sensor Process")
#    current_sensor_process = multiprocessing.Process(target=current_sensor_loop, args=(current_sensor_frequency,))

    # start the sensor processes
    #temperature_process.start()
    #humidity_process.start()
    accelerometer_process.start()
    #current_sensor_process.start()

    src.logs.log("[SENSORS] All sensor processes running!")
#    GPIO.output(accelerometer_status_led_pin, GPIO.HIGH)

    # check the sensor processes, exit if any are not alive
    while True:
        #if not temperature_process.is_alive():
        #    src.logs.log("[SENSORS] Temperature process died, restarting all")
        #    break
        #if not humidity_process.is_alive():
        #    src.logs.log("[SENSORS] Humidity process died, restarting all")
        #    break
        if not accelerometer_process.is_alive():
            src.logs.log("[SENSORS] Accelerometer process died, restarting all")
           # GPIO.output(accelerometer_status_led_pin, GPIO.LOW)
            break
        #if not current_sensor_process.is_alive():
        #    src.logs.log("[SENSORS] Current Sensor process died, restarting all")
        #    break
        
        git_check_flag = src.gitcheck.check_flag_file()
        if git_check_flag == "RESET":
            break

        # check time, for uploads at 10pm nightly
        update_flag = True
        current_hour = datetime.datetime.now().hour
        if current_hour == 22 and update_flag:
            src.logs.log("[SENSORS] Uploading files to Google Drive")
            print("accelerometer_" + src.logs.get_date() + ".data")
            time.sleep(5)
#            src.drive.upload_file("./data/accelerometer/accelerometer_" + src.logs.get_date() + ".data",
#                                  "'Sundar Lab'/data/accelerometer")
#            src.drive.upload_file("data/humidity/humidity" + src.logs.get_date() + ".data",
#                                  "'Sundar Lab'/data/humidity/")
#            src.drive.upload_file("data/temperature/temperature" + src.logs.get_date() + ".data",
#                                  "'Sundar Lab'/data/temperature/")
#            src.drive.upload_file("data/current/current" + src.logs.get_date() + ".data",
#                                  "'Sundar Lab'/data/current_sensor/")
#            src.drive.upload_file("data/logs/_log_pi_" + src.logs.get_date() + "",
#                                  "'Sundar Lab'/data/logs/")
            src.logs.log("[SENSORS] Completed uploading files to Google Drive")

            update_flag = False

        elif current_hour != 22 and not update_flag:
            update_flag = True

        time.sleep(5)

    # terminate the processes
#    temperature_process.terminate()
#    humidity_process.terminate()
    print("Resetting")
    accelerometer_process.terminate()
   # GPIO.output(accelerometer_status_led_pin, GPIO.LOW)
#    current_sensor_process.terminate()
    src.logs.log("[SENSORS] Terminated all sensor subprocesses")

    return
