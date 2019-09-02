#!/bin/bash

prog="/mnt/USB1/Growbox_Control/Growbox_Control.py"
checkProg="/usr/bin/python /mnt/USB1/Growbox_Control/Growbox_Control.py"
isRunning=`ps -edf | grep $prog | grep -v defunct | grep -v grep | awk '{print $2}'`
if["$isRunning" = ""]
then
    $prog &
fi
