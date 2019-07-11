# resets the webserver
echo Killing the webserver
# gets the PID
PID=$(lsof -i:5000 | awk 'FNR==2 { print $2 }')
# kills the PID
if [ "$PID" == "" ]; then
    echo Webserver not running
else
    echo Killing webserver
    kill $PID > /dev/null
    echo Webserver killed
fi
