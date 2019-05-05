import subprocess

print("starting")
ps = subprocess.Popen("./collect.o")
while True:
  print("restarting process")
  ps = subprocess.Popen("./collect.o")
  ps.wait()