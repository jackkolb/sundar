import shutil
import datetime
import zipfile
import os
import re
import os.path


# extracts the file dates from the raw files
def get_filedates():
    files = os.listdir("data/raw")
    dates = ["_".join(x.split("_")[1:4]) for x in files if len(x.split("_")) == 7]
    return dates, files


# clears the raw data folder of a certain date YYYY_MM_DD
def clear_data_folder(date):
    for root, dirs, files in os.walk("data/raw"):
        for file in files:
            if date in str(file):
                os.remove(os.path.join(root, file))
    return


# compresses the data in data/raw by date
def compress_data():
    now = datetime.datetime.now()
    dates, files = get_filedates()  # get dates of files
    zipped_dates = []
    for date in dates:
        # check if the file date is the current date, if so pass
        date_check = date.split("_")
        date_check_year = (date_check[0] == str(now.year)) 
        date_check_month = (date_check[1] == str(now.month) or date_check[1] == "0" + str(now.month))
        date_check_day = (date_check[2] == str(now.day) or date_check[2] == "0" + str(now.day))
        if not (date_check_year and date_check_month and date_check_day):  # if the dates are different
            # compress it
            with zipfile.ZipFile("data/daily/compressed_" + date + ".zip", mode="w") as zf:
                [zf.write("data/raw/" + f) for f in files if date in f]

            # add date to the zipped date list
            zipped_dates.append(date)  

    # go through the dates that were zipped 
    for date in zipped_dates:
        # clear those files from the data folder
        clear_data_folder(date)
        
    return
