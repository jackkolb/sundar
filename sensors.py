import time
import logs
import threading


# reads data from the temperature sensor
def temperature_sensor_poll():
    return 75


# continuously polls the temperature sensor as per the specified frequency
def temperature_sensor_loop(frequency):
    while True:
        with open("data/temperature.data", "w") as temperature_data_file:
            temperature_reading = temperature_sensor_poll()
            timestamp = time.time()
            temperature_data_file.write(str(timestamp) + ", " + str(temperature_reading))

        time.sleep(1/frequency)


# reads data from the humidity sensor
def humidity_sensor_poll():
    return 83


# continuously polls the humidity sensor as per the specified frequency
def humidity_sensor_loop(frequency):
    while True:
        with open("data/humidity.data", "w") as humidity_data_file:
            humidity_reading = humidity_sensor_poll()
            timestamp = time.time()
            humidity_data_file.write(str(timestamp) + ", " + str(humidity_reading))

        time.sleep(1 / frequency)


# reads data from the accelerometer
def accelerometer_sensor_poll():
    return 2


# continuously polls the accelerometer as per the specified frequency
def accelerometer_sensor_loop(frequency):
    while True:
        with open("data/accelerometer.data", "w") as accelerometer_data_file:
            accelerometer_reading = accelerometer_sensor_poll()
            timestamp = time.time()
            accelerometer_data_file.write(str(timestamp) + ", " + str(accelerometer_reading))

        time.sleep(1 / frequency)


# reads data from the current sensor
def current_sensor_poll():
    return 2


# continuously polls the current sensor as per the specified frequency
def current_sensor_loop(frequency):
    while True:
        with open("data/current.data", "w") as current_data_file:
            current_reading = accelerometer_sensor_poll()
            timestamp = time.time()
            current_data_file.write(str(timestamp) + ", " + str(current_reading))

        time.sleep(1 / frequency)


def sensor_manager(settings):
    # get the sensor frequencies from the settings
    temperature_frequency = settings["TEMPERATURE_FREQUENCY"]
    humidity_frequency = settings["HUMIDITY_FREQUENCY"]
    accelerometer_frequency = settings["ACCELEROMETER_FREQUENCY"]
    current_sensor_frequency = settings["CURRENT_SENSOR_FREQUENCY"]

    # create the sensor threads
    temperature_thread = threading.Thread(target=temperature_sensor_loop, args=(temperature_frequency,))
    humidity_thread = threading.Thread(target=humidity_sensor_loop, args=(humidity_frequency,))
    accelerometer_thread = threading.Thread(target=accelerometer_sensor_loop, args=(accelerometer_frequency,))
    current_sensor_thread = threading.Thread(target=current_sensor_loop, args=(current_sensor_frequency,))

    # start the sensor threads
    temperature_thread.start()
    humidity_thread.start()
    accelerometer_thread.start()
    current_sensor_thread.start()

    return