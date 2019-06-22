import math

with open("data.txt", "r") as data:
	lines = data.readlines()

min_dist_p = 10000
mxp = -1
myp = -1
zp = -1

min_dist_n = 100000
mxn = -1
myn = -1
zn = -1

g = []

for line in lines:
	d = line.split(":")
	if len(d) != 2:
		continue
	d = d[1].split(",")
	if len(d) != 3:
		continue
	x = int(d[0])
	y = int(d[1])
	z = int(d[2][:-1])
	
	if x == 0 or y == 0:
		g.append(math.sqrt(x*x+y*y+z*z))
	
	if math.sqrt(x*x + y*y) < min_dist_p and z > 0:
		zp = z
		min_dist_p = math.sqrt(x*x + y*y)
		mxp = x
		myp = y
		
	if math.sqrt(x*x + y*y) < min_dist_n and z < 0:
		zn = z
		min_dist_n = math.sqrt(x*x + y*y)
		mxn = x
		myn = y

print(zp)
print(min_dist_p)
print(mxp)
print(myp)

print()

print(zn)
print(min_dist_n)
print(mxn)
print(myn)

print()
print(len(g))
print(sum(g)/len(g))