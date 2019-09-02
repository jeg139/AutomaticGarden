#!/usr/bin/python
# coding: utf8

import ctypes
import subprocess
import time
import signal

libc = ctypes.CDLL('/lib/arm-linux-gnueabihf/libc.so.6')
PR_SET_PDEATHSIG = 1
SIGINT = 2
SIGTERM = 15
# class
# Class pour un arrêt propre
class GracefulKiller:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)
    def exit_gracefully(self, signum, frame):
        self.kill_now = True
# Fonctions
# Fonctions avec les signaux d'arrêt
def set_death_signal(signal):
    libc.prctl(PR_SET_PDEATHSIG, signal)
def set_death_signal_int():
    set_death_signal(SIGINT)
def set_death_signal_term():
    set_death_signal(SIGTERM)
def exit_gracefully(self, signum, frame):
    self.kill_now = True
def start_processus():
    pidGrowboxSerial = subprocess.Popen(['/mnt/USB1/Growbox_Control/Growbox_Serial.py'], preexec_fn=set_death_signal_int).pid
    pidGrowboxSerial = pidStartGrowboxSerial = str(pidGrowboxSerial)
    with open('/mnt/USB1/Growbox_Control/Variable/pidStartGrowboxSerial.txt', 'w') as fichier:
        fichier.seek(0)
        fichier.write(pidStartGrowboxSerial)
        fichier.truncate()
    with open('/mnt/USB1/Growbox_Control/Variable/pidGrowboxSerial.txt', 'w') as fichier:
        fichier.seek(0)
        fichier.write(pidGrowboxSerial)
        fichier.truncate()
    pidGrowboxSensor = pidStartGrowboxSensor = subprocess.Popen(['/mnt/USB1/Growbox_Control/Growbox_Sensor.py'], preexec_fn=set_death_signal_int).pid # Ouvrir un sous-processus et récupérer son PID
    pidGrowboxSensor = pidStartGrowboxSensor = str(pidGrowboxSensor)
    with open('/mnt/USB1/Growbox_Control/Variable/pidStartGrowboxSensor.txt', 'w') as fichier:
        fichier.seek(0)
        fichier.write(pidStartGrowboxSensor)
        fichier.truncate()
    with open('/mnt/USB1/Growbox_Control/Variable/pidGrowboxSensor.txt', 'w') as fichier:
        fichier.seek(0)
        fichier.write(pidGrowboxSensor)
        fichier.truncate()
    pidGrowboxTimeEvent = subprocess.Popen(['/mnt/USB1/Growbox_Control/Growbox_Time_Event.py'], preexec_fn=set_death_signal_int).pid
    pidGrowboxTimeEvent = pidStartGrowboxTimeEvent = str(pidGrowboxTimeEvent)
    with open('/mnt/USB1/Growbox_Control/Variable/pidStartGrowboxTimeEvent.txt', 'w') as fichier:
        fichier.seek(0)
        fichier.write(pidStartGrowboxTimeEvent)
        fichier.truncate()
    with open('/mnt/USB1/Growbox_Control/Variable/pidGrowboxTimeEvent.txt', 'w') as fichier:
        fichier.seek(0)
        fichier.write(pidGrowboxTimeEvent)
        fichier.truncate()
    pidGrowboxMenu = subprocess.Popen(['/mnt/USB1/Growbox_Control/Growbox_Menu.py'], preexec_fn=set_death_signal_int).pid
    pidGrowboxMenu = pidStartGrowboxMenu = str(pidGrowboxMenu)
    with open('/mnt/USB1/Growbox_Control/Variable/pidStartGrowboxMenu.txt', 'w') as fichier:
        fichier.seek(0)
        fichier.write(pidStartGrowboxMenu)
        fichier.truncate()
    with open('/mnt/USB1/Growbox_Control/Variable/pidGrowboxMenu.txt', 'w') as fichier:
        fichier.seek(0)
        fichier.write(pidGrowboxMenu)
        fichier.truncate()
def surveillance_processus():
    with open('/mnt/USB1/Growbox_Control/Variable/pidStartGrowboxSensor.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        pidStartGrowboxSensor = fichier.read(4)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/pidStartGrowboxSerial.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        pidStartGrowboxSerial = fichier.read(4)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/pidStartGrowboxTimeEvent.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        pidStartGrowboxTimeEvent = fichier.read(4)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/pidStartGrowboxMenu.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        pidStartGrowboxMenu = fichier.read(4)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/pidGrowboxSensor.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        pidGrowboxSensor = fichier.read(4)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/pidGrowboxSerial.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        pidGrowboxSerial = fichier.read(4)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/pidGrowboxTimeEvent.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        pidGrowboxTimeEvent = fichier.read(4)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/pidGrowboxMenu.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        pidGrowboxMenu = fichier.read(4)
        fichier.close()
    if(pidGrowboxSensor == pidStartGrowboxSensor and pidGrowboxSerial == pidStartGrowboxSerial and
       pidGrowboxTimeEvent == pidStartGrowboxTimeEvent and pidGrowboxMenu == pidStartGrowboxMenu):
        ouputGrowboxSerial = subprocess.Popen(['pgrep', '-f', '/usr/bin/python /mnt/USB1/Growbox_Control/Growbox_Serial.py'], stdout=subprocess.PIPE)
        pidGrowboxSerial = ouputGrowboxSerial.stdout.read()
        with open('/mnt/USB1/Growbox_Control/Variable/pidGrowboxSerial.txt', 'w') as fichier:
            fichier.seek(0)
            fichier.write(pidGrowboxSerial)
            fichier.truncate()
        ouputGrowboxSensor = subprocess.Popen(['pgrep', '-f', '/usr/bin/python /mnt/USB1/Growbox_Control/Growbox_Sensor.py'], stdout=subprocess.PIPE)
        pidGrowboxSensor = ouputGrowboxSensor.stdout.read()
        with open('/mnt/USB1/Growbox_Control/Variable/pidGrowboxSensor.txt', 'w') as fichier:
            fichier.seek(0)
            fichier.write(pidGrowboxSensor)
            fichier.truncate()
        ouputGrowboxTimeEvent = subprocess.Popen(['pgrep', '-f', '/usr/bin/python /mnt/USB1/Growbox_Control/Growbox_Time_Event.py'], stdout=subprocess.PIPE)
        pidGrowboxTimeEvent = ouputGrowboxTimeEvent.stdout.read()
        with open('/mnt/USB1/Growbox_Control/Variable/pidGrowboxTimeEvent.txt', 'w') as fichier:
            fichier.seek(0)
            fichier.write(pidGrowboxTimeEvent)
            fichier.truncate()
        ouputGrowboxMenu = subprocess.Popen(['pgrep', '-f', '/usr/bin/python /mnt/USB1/Growbox_Control/Growbox_Menu.py'], stdout=subprocess.PIPE)
        pidGrowboxMenu = ouputGrowboxMenu.stdout.read()
        with open('/mnt/USB1/Growbox_Control/Variable/pidGrowboxMenu.txt', 'w') as fichier:
            fichier.seek(0)
            fichier.write(pidGrowboxMenu)
            fichier.truncate()
    elif(pidGrowboxSensor != pidStartGrowboxSensor or pidGrowboxSerial != pidStartGrowboxSerial or
         pidGrowboxTimeEvent != pidStartGrowboxTimeEvent or pidGrowboxMenu != pidStartGrowboxMenu):
        if(pidGrowboxSerial != pidStartGrowboxSerial):
            pidGrowboxSerial = subprocess.Popen(['/mnt/USB1/Growbox_Control/Growbox_Serial.py'], preexec_fn=set_death_signal_int).pid
            pidGrowboxSerial = pidStartGrowboxSerial = str(pidGrowboxSerial)
            with open('/mnt/USB1/Growbox_Control/Variable/pidStartGrowboxSerial.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write(pidStartGrowboxSerial)
                fichier.truncate()
            with open('/mnt/USB1/Growbox_Control/Variable/pidGrowboxSerial.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write(pidGrowboxSerial)
                fichier.truncate()
        if(pidGrowboxSensor != pidStartGrowboxSensor):
            pidStartGrowboxSensor = subprocess.Popen(['/mnt/USB1/Growbox_Control/Growbox_Sensor.py'], preexec_fn=set_death_signal_int).pid
            pidGrowboxSensor = pidStartGrowboxSensor = str(pidGrowboxSensor)
            with open('/mnt/USB1/Growbox_Control/Variable/pidStartGrowboxSensor.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write(pidStartGrowboxSensor)
                fichier.truncate()
            with open('/mnt/USB1/Growbox_Control/Variable/pidGrowboxSensor.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write(pidGrowboxSensor)
                fichier.truncate()
        if(pidGrowboxTimeEvent != pidStartGrowboxTimeEvent):
            pidGrowboxTimeEvent = subprocess.Popen(['/mnt/USB1/Growbox_Control/Growbox_Time_Event.py'], preexec_fn=set_death_signal_int).pid
            pidGrowboxTimeEvent = pidStartGrowboxTimeEvent = str(pidGrowboxTimeEvent)
            with open('/mnt/USB1/Growbox_Control/Variable/pidStartGrowboxTimeEvent.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write(pidStartGrowboxTimeEvent)
                fichier.truncate()
            with open('/mnt/USB1/Growbox_Control/Variable/pidGrowboxTimeEvent.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write(pidGrowboxTimeEvent)
                fichier.truncate()
        if(pidGrowboxMenu != pidStartGrowboxMenu):
            pidGrowboxMenu = subprocess.Popen(['/mnt/USB1/Growbox_Control/Growbox_Menu.py'], preexec_fn=set_death_signal_int).pid
            pidGrowboxMenu = pidStartGrowboxMenu = str(pidGrowboxMenu)
            with open('/mnt/USB1/Growbox_Control/Variable/pidStartGrowboxMenu.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write(pidStartGrowboxMenu)
                fichier.truncate()
            with open('/mnt/USB1/Growbox_Control/Variable/pidGrowboxMenu.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write(pidGrowboxMenu)
                fichier.truncate()
# Programme principal
killer = GracefulKiller()
start_processus()
while not killer.kill_now:
    surveillance_processus()
    time.sleep(2)
