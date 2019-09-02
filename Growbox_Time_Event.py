#!/usr/bin/python
# coding: utf8

import datetime
import time
import signal
# class
# Class pour un arrêt propre
class GracefulKiller:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)
    def exit_gracefully(self, signum, frame):
        self.kill_now = True
# definition
def commande_lampe_cro():
    dateNow = datetime.datetime.now()
    dateNow = dateNow.time()
    todayCroStart = dateNow.replace(hour=20, minute=0, second=0, microsecond=0)
    todayCroEnd = dateNow.replace(hour=14, minute=0, second=0, microsecond=0)
    todayCompareStartSeven = dateNow.replace(hour=7, minute=0, second=0, microsecond=0)
    todayCompareStartSix = dateNow.replace(hour=6, minute=0, second=0, microsecond=0)
    today0 = dateNow.replace(hour=0, minute=0, second=0, microsecond=0)
    if(todayCroStart >= todayCompareStartSeven):
        if(dateNow >= todayCroStart):
            with open('/mnt/USB1/Growbox_Control/Variable/lampe.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('1')
                fichier.truncate()
        elif(dateNow >= today0 and dateNow <= todayCroEnd):
            with open('/mnt/USB1/Growbox_Control/Variable/lampe.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('1')
                fichier.truncate()
        elif(dateNow > todayCroEnd and dateNow < todayCroStart):
            with open('/mnt/USB1/Growbox_Control/Variable/lampe.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('S1')
                fichier.truncate()
    elif(todayCroStart <= todayCompareStartSix):
        if(dateNow >= todayCroStart):
            with open('/mnt/USB1/Growbox_Control/Variable/lampe.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('1')
                fichier.truncate()
        elif(dateNow > todayCroEnd or dateNow < todayCroStart):
            with open('/mnt/USB1/Growbox_Control/Variable/lampe.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('S1')
                fichier.truncate()
def commande_lampe_flo():
    dateNow = datetime.datetime.now()
    dateNow = dateNow.time()
    todayFloStart = dateNow.replace(hour=20, minute=0, second=0, microsecond=0)
    todayFloEnd = dateNow.replace(hour=8, minute=0, second=0, microsecond=0)
    todayCompareStartThirteen = dateNow.replace(hour=13, minute=0, second=0, microsecond=0)
    todayCompareStarttwelve = dateNow.replace(hour=12, minute=0, second=0, microsecond=0)
    today0 = dateNow.replace(hour=0, minute=0, second=0, microsecond=0)
    if(todayFloStart >= todayCompareStartThirteen):
        if(dateNow >= todayFloStart):
            with open('/mnt/USB1/Growbox_Control/Variable/lampe.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('1')
                fichier.truncate()
        elif(dateNow >= today0 and dateNow <= todayFloEnd):
            with open('/mnt/USB1/Growbox_Control/Variable/lampe.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('1')
                fichier.truncate()
        elif(dateNow > todayFloEnd and dateNow < todayFloStart):
            with open('/mnt/USB1/Growbox_Control/Variable/lampe.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('S1')
                fichier.truncate()
    elif(todayFloStart <= todayCompareStarttwelve):
        if(dateNow >= todayFloStart):
            with open('/mnt/USB1/Growbox_Control/Variable/lampe.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('1')
                fichier.truncate()
        elif(dateNow > todayFloEnd or dateNow < todayFloStart):
            with open('/mnt/USB1/Growbox_Control/Variable/lampe.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('S1')
                fichier.truncate()
def commande_ventilateur_cro():
    dateNow = datetime.datetime.now()
    dateNow = dateNow.time()
    todayCroStart = dateNow.replace(hour=20, minute=0, second=0, microsecond=0)
    todayCroEnd = dateNow.replace(hour=14, minute=0, second=0, microsecond=0)
    todayCompareStartSeven = dateNow.replace(hour=7, minute=0, second=0, microsecond=0)
    todayCompareStartSix = dateNow.replace(hour=6, minute=0, second=0, microsecond=0)
    today0 = dateNow.replace(hour=0, minute=0, second=0, microsecond=0)
    if(todayCroStart >= todayCompareStartSeven):
        if(dateNow >= todayCroStart):
            with open('/mnt/USB1/Growbox_Control/Variable/ventilateur.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('4')
                fichier.truncate()
        elif(dateNow >= today0 and dateNow <= todayCroEnd):
            with open('/mnt/USB1/Growbox_Control/Variable/ventilateur.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('4')
                fichier.truncate()
        elif(dateNow > todayCroEnd and dateNow < todayCroStart):
            with open('/mnt/USB1/Growbox_Control/Variable/ventilateur.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('S4')
                fichier.truncate()
    elif(todayCroStart <= todayCompareStartSix):
        if(dateNow >= todayCroStart):
            with open('/mnt/USB1/Growbox_Control/Variable/ventilateur.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('4')
                fichier.truncate()
        elif(dateNow > todayCroEnd or dateNow < todayCroStart):
            with open('/mnt/USB1/Growbox_Control/Variable/ventilateur.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('S4')
                fichier.truncate()
def commande_ventilateur_flo():
    dateNow = datetime.datetime.now()
    dateNow = dateNow.time()
    todayFloStart = dateNow.replace(hour=20, minute=0, second=0, microsecond=0)
    todayFloEnd = dateNow.replace(hour=8, minute=0, second=0, microsecond=0)
    todayCompareStartThirteen = dateNow.replace(hour=13, minute=0, second=0, microsecond=0)
    todayCompareStarttwelve = dateNow.replace(hour=12, minute=0, second=0, microsecond=0)
    today0 = dateNow.replace(hour=0, minute=0, second=0, microsecond=0)
    if(todayFloStart >= todayCompareStartThirteen):
        if(dateNow >= todayFloStart):
            with open('/mnt/USB1/Growbox_Control/Variable/ventilateur.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('4')
                fichier.truncate()
        elif(dateNow >= today0 and dateNow <= todayFloEnd):
            with open('/mnt/USB1/Growbox_Control/Variable/ventilateur.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('4')
                fichier.truncate()
        elif(dateNow > todayFloEnd and dateNow < todayFloStart):
            with open('/mnt/USB1/Growbox_Control/Variable/ventilateur.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('S4')
                fichier.truncate()
    elif(todayFloStart <= todayCompareStarttwelve):
        if(dateNow >= todayFloStart):
            with open('/mnt/USB1/Growbox_Control/Variable/ventilateur.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('4')
                fichier.truncate()
        elif(dateNow > todayFloEnd or dateNow < todayFloStart):
            with open('/mnt/USB1/Growbox_Control/Variable/ventilateur.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write('S4')
                fichier.truncate()
def commande_intracteur_extracteur():
    dateNow = datetime.datetime.now()
    dateNow = dateNow.time()
    if(dateNow == dateNow):
        with open('/mnt/USB1/Growbox_Control/Variable/intractionExtractionAir.txt', 'w') as fichier:
            fichier.seek(0)
            fichier.write('2')
            fichier.truncate()
# Programme principal
killer = GracefulKiller()
while not killer.kill_now:
    commande_lampe_cro()
    #commande_lampe_flo()
    commande_ventilateur_cro()
    #commande_ventilateur_flo()
    commande_intracteur_extracteur()
    time.sleep(3)
