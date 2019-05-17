# asks for a file (in the format of our data)
# downsamples it to 1000Hz


print("Downsampling Script for Sundar's Lab")
print("Will downsample to 1000Hz")
file_name = input("Enter the file name (in this directory): ")
input("Press enter to start")

new_data = []

print("processing input file")

with open(file_name, "r") as data_file:
    time_marker = 0
    for line in data_file.readlines():
        time = int(line.split(":")[0])
        time = int(time / 1000)
        if time > time_marker:
            new_data.append(line)
            time_marker = time

print("writing to output file (downsampled_data.txt)")

with open("./downsampled_data.txt", "w") as output_file:
    for line in new_data:
        output_file.write(line)

