#/bin/sh

cd "$(dirname "$0")"
#echo Launching Webserver
#bash -c "cd ~/projects/sundar/www/node; ./node.sh" &

echo Launching Loader
python3 ./src/py/loader.py

#echo Resetting Webserver
#./reset.sh