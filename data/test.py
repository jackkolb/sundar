import math

with open("data.txt", "r") as data:
	lines = data.readlines()
min_dist = 10000
mx = -1
my = -1
z = -1

for line in lines:
	d = line.split(":")
	if len(d) != 2:
		continue
	d = d[1].split(",")
	if len(d) != 3:
		continue
	x = int(d[0])
	y = int(d[1])
	test_z = int(d[2][:-1])
	if math.sqrt(x*x + y*y) < min_dist and test_z != 0:
		z = test_z
		min_dist = math.sqrt(x*x + y*y)
		mx = x
		my = y
		
print(z)
print(min_dist)
print(mx)
print(my)