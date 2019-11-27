import subprocess
import multiprocessing

def scan(i):
  subprocess.call(["/home/jack/projects/sundar/scan_network.sh", str(i), str(i)])

if __name__ == "__main__":
  for i in range(0, 256):
    p = multiprocessing.Process(target=scan, args=[i,])
    p.start()


