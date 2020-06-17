# updates all the pip packages (not run automatically)
pip3 install -U $(pip freeze | awk '{split($0, a, "=="); print a[1]}')