#!/bin/sh
### BEGIN INIT INFO
# Provides:          sensor stuff
# Required-Start:    $local_fs
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: starts sensor
# Description:       runs an http server and python script to run sensors
### END INIT INFO

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting server "
    python /home/beaglesensors/server.py &
    # example 1 - system service
    # /usr/bin/foobar --config /etc/foo.conf start

    # example 2 - run script as user
    # su --login mkaz --command "/home/mkaz/bin/my-script --cmd-args"
    
    ;;
  stop)
    echo "Stopping server"
    pid=`ps guax | grep server.py | grep -v grep | awk '{print $2}'`
    kill $pid
    # example 1
    # /usr/bin/foobar --config /etc/foo.conf stop

    ;;
  *)
    echo "Usage: /etc/init.d/server.py {start|stop}"
    exit 1
    ;;
esac

exit 0
