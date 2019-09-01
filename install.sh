# installs the requirements (assumes the GitHub has been cloned)

# from package manager:
#   lsop
sudo apt-get install lsop


# from python:
#   flask (webserver)
#   RPLCD (16x2 LCD display)
#   numpy (fft and machine learning)
sudo pip3 install flask, RPLCD, numpy

# create data/accelerometer.data
touch data/accelerometer.data

# create data/raw/ folder
mkdir data/raw
