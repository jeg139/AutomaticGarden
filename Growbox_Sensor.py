#!/usr/bin/python
# coding: utf8

import math
import time
import signal
import os
# class
# Class pour un arrêt propre
class GracefulKiller:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)
    def exit_gracefully(self, signum, frame):
        self.kill_now = True
# Definition
# Fontion capteur temperature et humidite
def temperature_humidite():
    try:
        fichierRepTempHum = '/mnt/USB1/Growbox_Control/Variable/temperatureHumidite.txt'
        tailleTempHum = os.path.getsize(fichierRepTempHum)
        if(tailleTempHum != 0):
            with open('/mnt/USB1/Growbox_Control/Variable/temperatureHumidite.txt', 'r') as fichier:
                d = fichier.readlines()
                fichier.seek(0)
                temperature = fichier.read(2)
                fichier.close()
            with open('/mnt/USB1/Growbox_Control/Variable/temperatureHumidite.txt', 'r') as fichier:
                d = fichier.readlines()
                fichier.seek(2)
                humidite = fichier.read(2)
                fichier.close()
            with open('/mnt/USB1/Growbox_Control/Variable/precedenteTemperature.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write(temperature)
                fichier.truncate()
            with open('/mnt/USB1/Growbox_Control/Variable/precedenteHumidite.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write(humidite)
                fichier.truncate()
        fichierRepPrecedenteTemp = '/mnt/USB1/Growbox_Control/Variable/precedenteTemperature.txt'
        fichierRepPrecedenteHum = '/mnt/USB1/Growbox_Control/Variable/precedenteHumidite.txt'
        taillePrecedenteTemp = os.path.getsize(fichierRepPrecedenteTemp)
        taillePrecedenteHum = os.path.getsize(fichierRepPrecedenteHum)
        if(taillePrecedenteTemp != 0 and taillePrecedenteHum != 0):
            with open('/mnt/USB1/Growbox_Control/Variable/precedenteTemperature.txt', 'r') as fichier:
                d = fichier.readlines()
                fichier.seek(0)
                precedenteTemperature = fichier.read(2)
                fichier.close()
            with open('/mnt/USB1/Growbox_Control/Variable/precedenteHumidite.txt', 'r') as fichier:
                d = fichier.readlines()
                fichier.seek(0)
                precedenteHumidite = fichier.read(2)
                fichier.close()
        temperature = int(temperature)
        humidite = int(humidite)
        precedenteTemperature = int(precedenteTemperature)
        precedenteHumidite = int(precedenteHumidite)
        if(temperature != precedenteTemperature or humidite != precedenteHumidite):
            if(temperature > 24 or humidite > 70):
                with open('/mnt/USB1/Growbox_Control/Variable/ventilateurTemperature.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write('3')
                    fichier.truncate()
            elif(temperature <= 24 and humidite <= 70):
                with open('/mnt/USB1/Growbox_Control/Variable/ventilateurTemperature.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write('S3')
                    fichier.truncate()
    except (ValueError, TypeError, AttributeError):
        return
# Fonction capteur humidite terre
def humidite_terreau():
    try:
        fichierRepHumTerreau = '/mnt/USB1/Growbox_Control/Variable/humiditeTerreau.txt'
        tailleHumTerreau = os.path.getsize(fichierRepHumTerreau)
        fichierRepNivReservoir = '/mnt/USB1/Growbox_Control/Variable/niveauReservoir.txt'
        tailleNivReservoir = os.path.getsize(fichierRepNivReservoir)
        if(tailleHumTerreau != 0 and tailleNivReservoir != 0):
            with open('/mnt/USB1/Growbox_Control/Variable/humiditeTerreau.txt', 'r') as fichier:
                d = fichier.readlines()
                fichier.seek(0)
                humiditeTerreau = fichier.read()
                fichier.close()
            humiditeTerreau = float(humiditeTerreau)
            humiditeTerreau = math.trunc(humiditeTerreau)
            humiditeTerreau = int(humiditeTerreau)
            with open('/mnt/USB1/Growbox_Control/Variable/niveauReservoir.txt', 'r') as fichier:
                d = fichier.readlines()
                fichier.seek(0)
                niveauReservoir = fichier.read()
                fichier.close()
            niveauReservoir = float(niveauReservoir)
            niveauReservoir = math.trunc(niveauReservoir)
            niveauReservoir = int(niveauReservoir)
            if(humiditeTerreau > 550 and niveauReservoir < 550):
                with open('/mnt/USB1/Growbox_Control/Variable/pompeEau.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write('5')
                    fichier.truncate()
                with open('/mnt/USB1/Growbox_Control/Variable/niveauBasReservoir.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write('Reservoir Ok')
                    fichier.truncate()
            elif(humiditeTerreau <= 550 and niveauReservoir <= 550):
                with open('/mnt/USB1/Growbox_Control/Variable/pompeEau.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write('S5')
                    fichier.truncate()
                with open('/mnt/USB1/Growbox_Control/Variable/niveauBasReservoir.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write('Reservoir Ok')
                    fichier.truncate()
            elif(humiditeTerreau <= 550 and niveauReservoir > 550):
                with open('/mnt/USB1/Growbox_Control/Variable/pompeEau.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write('S5')
                    fichier.truncate()
                with open('/mnt/USB1/Growbox_Control/Variable/niveauBasReservoir.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write('Reservoir vide')
                    fichier.truncate()
            elif(humiditeTerreau > 550 and niveauReservoir > 550):
                with open('/mnt/USB1/Growbox_Control/Variable/pompeEau.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write('S5')
                    fichier.truncate()
                with open('/mnt/USB1/Growbox_Control/Variable/niveauBasReservoir.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write('Reservoir vide Alert!')
                    fichier.truncate()
    except (ValueError, TypeError, AttributeError):
        return
def luminosite_box():
    try:
        fichierRepLuminosite = '/mnt/USB1/Growbox_Control/Variable/luminosite.txt'
        tailleLuminosite = os.path.getsize(fichierRepLuminosite)
        fichierRepLampe = '/mnt/USB1/Growbox_Control/Variable/lampe.txt'
        tailleLampe = os.path.getsize(fichierRepLampe)
        if(tailleLuminosite != 0 and tailleLampe != 0):
            with open('/mnt/USB1/Growbox_Control/Variable/luminosite.txt', 'r') as fichier:
                d = fichier.readlines()
                fichier.seek(0)
                luminositeBox = fichier.read(7)
                fichier.close()
            luminositeBox = float(luminositeBox)
            luminositeBox = math.trunc(luminositeBox)
            luminositeBox = int(luminositeBox)
            with open('/mnt/USB1/Growbox_Control/Variable/lampe.txt', 'r') as fichier:
                d = fichier.readlines()
                fichier.seek(0)
                relaiLampe = fichier.read(2)
                fichier.close()
            if(luminositeBox <= 500 and relaiLampe == '1'):
                with open('/mnt/USB1/Growbox_Control/Variable/etatAmpoule.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write('La lumière est Allumée.')
                    fichier.truncate()
            elif(luminositeBox > 500  and relaiLampe == '1'):
                with open('/mnt/USB1/Growbox_Control/Variable/etatAmpoule.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write('La lumière ne s\'est pas allumée.')
                    fichier.truncate()
            elif(luminositeBox <= 500 and relaiLampe == 'S1'):
                with open('/mnt/USB1/Growbox_Control/Variable/etatAmpoule.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write('La lumière ne s\'est pas éteinte.')
                    fichier.truncate()
            elif(luminositeBox > 500 and relaiLampe == 'S1'):
                with open('/mnt/USB1/Growbox_Control/Variable/etatAmpoule.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write('La lumière est éteinte.')
                    fichier.truncate()
    except (ValueError, TypeError, AttributeError):
        return
#Programme principal
killer = GracefulKiller()
while not killer.kill_now:
    temperature_humidite()
    humidite_terreau()
    luminosite_box()
    time.sleep(3)
