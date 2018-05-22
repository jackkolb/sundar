import time
import logs
import multiprocessing


# reads data from the temperature sensor
def temperature_sensor_poll():
    return 75


# continuously polls the temperature sensor as per the specified frequency
def temperature_sensor_loop(frequency):
    while True:
        with open("data/temperature.data", "a") as temperature_data_file:
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
        with open("data/humidity.data", "a") as humidity_data_file:
            humidity_reading = humidity_sensor_poll()
            timestamp = time.time()
            humidity_data_file.write(str(timestamp) + ", " + str(humidity_reading) + "\n")

        time.sleep(1.0 / float(frequency))


# reads data from the accelerometer
def accelerometer_sensor_poll():
    return 2


# continuously polls the accelerometer as per the specified frequency
def accelerometer_sensor_loop(frequency):
    while True:
        with open("data/accelerometer.data", "a") as accelerometer_data_file:
            accelerometer_reading = accelerometer_sensor_poll()
            timestamp = time.time()
            accelerometer_data_file.write(str(timestamp) + ", " + str(accelerometer_reading) + "\n")

        time.sleep(1.0 / float(frequency))


# reads data from the current sensor
def current_sensor_poll():
    return 2


# continuously polls the current sensor as per the specified frequency
def current_sensor_loop(frequency):
    while True:
        with open("data/current.data", "a") as current_data_file:
            current_reading = accelerometer_sensor_poll()
            timestamp = time.time()
            current_data_file.write(str(timestamp) + ", " + str(current_reading) + "\n")

        time.sleep(1.0 / float(frequency))


# manages the sensor processes
def sensor_manager(settings):
    # get the sensor frequencies from the settings
    temperature_frequency = settings["TEMPERATURE_FREQUENCY"]
    humidity_frequency = settings["HUMIDITY_FREQUENCY"]
    accelerometer_frequency = settings["ACCELEROMETER_FREQUENCY"]
    current_sensor_frequency = settings["CURRENT_SENSOR_FREQUENCY"]

    # create the sensor processes
    logs.log("[SENSORS] Starting Temperature Process")
    temperature_process = multiprocessing.Process(target=temperature_sensor_loop, args=(temperature_frequency,))
    logs.log("[SENSORS] Starting Humidity Process")
    humidity_process = multiprocessing.Process(target=humidity_sensor_loop, args=(humidity_frequency,))
    logs.log("[SENSORS] Starting Accelerometer Process")
    accelerometer_process = multiprocessing.Process(target=accelerometer_sensor_loop, args=(accelerometer_frequency,))
    logs.log("[SENSORS] Starting Current Sensor Process")
    current_sensor_process = multiprocessing.Process(target=current_sensor_loop, args=(current_sensor_frequency,))

    # start the sensor processes
    temperature_process.start()
    humidity_process.start()
    accelerometer_process.start()
    current_sensor_process.start()

    logs.log("[SENSORS] All sensor processes running!")

    # check the sensor processes, exit if any are not alive
    while True:
        if not temperature_process.is_alive():
            logs.log("[SENSORS] Temperature process died, restarting all")
            break
        if not humidity_process.is_alive():
            logs.log("[SENSORS] Humidity process died, restarting all")
            break
        if not accelerometer_process.is_alive():
            logs.log("[SENSORS] Accelerometer process died, restarting all")
            break
        if not current_sensor_process.is_alive():
            logs.log("[SENSORS] Current Sensor process died, restarting all")

        time.sleep(5)

    # terminate the processes
    temperature_process.terminate()
    humidity_process.terminate()
    accelerometer_process.terminate()
    current_sensor_process.terminate()
    logs.log("[SENSORS] Terminated all sensor subprocesses")

    return
