#!/usr/bin/python
# coding: utf8

import serial
import time
import signal
import math
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
def open_portcom():
    if not(portCom.is_open):
        try:
            portCom.open()
        except:
            print('Impossible de se connecter au port série')
def commande_arduino_firstloop():
    with open('/mnt/USB1/Growbox_Control/Variable/intractionExtractionAir.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        dernierRelaiActiverIntracteurExtracteur = fichier.read(2)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/ventilateurTemperature.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        dernierRelaiActiverVentilateurTemperature = fichier.read(2)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/lampe.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        dernierRelaiActiverLampe = fichier.read(2)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/ventilateur.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        dernierRelaiActiverVentilateur = fichier.read(2)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/pompeEau.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        dernierRelaiActiverPompe = fichier.read(2)
        fichier.close()
    if(dernierRelaiActiverIntracteurExtracteur == '2'):
        retour = ''
        while(retour != 'messageOk'):
            try:
                portCom.write(dernierRelaiActiverIntracteurExtracteur)
                time.sleep(1)
                nbCar = portCom.in_waiting
                retour = portCom.read(nbCar)
                with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiIntracteurExtracteur.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write(dernierRelaiActiverIntracteurExtracteur)
                    fichier.truncate()
                portCom.flushInput()
            except:
                portCom.flushInput()
    if(dernierRelaiActiverVentilateurTemperature == '3'):
        retour = ''
        while(retour != 'messageOk'):
            try:
                portCom.write(dernierRelaiActiverVentilateurTemperature)
                time.sleep(1)
                nbCar = portCom.in_waiting
                retour = portCom.read(nbCar)
                with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiVentilateurTemperature.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write(dernierRelaiActiverVentilateurTemperature)
                    fichier.truncate()
                portCom.flushInput()
            except:
                portCom.flushInput()
    if(dernierRelaiActiverLampe == '1'):
        retour = ''
        while(retour != 'messageOk'):
            try:
                portCom.write(dernierRelaiActiverLampe)
                time.sleep(1)
                nbCar = portCom.in_waiting
                retour = portCom.read(nbCar)
                with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiLampe.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write(dernierRelaiActiverLampe)
                    fichier.truncate()
                portCom.flushInput()
            except:
                portCom.flushInput()
    if(dernierRelaiActiverVentilateur == '4'):
        retour = ''
        while(retour != 'messageOk'):
            try:
                portCom.write(dernierRelaiActiverVentilateur)
                time.sleep(1)
                nbCar = portCom.in_waiting
                retour = portCom.read(nbCar)
                with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiVentilateur.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write(dernierRelaiActiverVentilateur)
                    fichier.truncate()
                portCom.flushInput()
            except:
                portCom.flushInput()
    if(dernierRelaiActiverPompe == '5'):
        retour = ''
        while(retour != 'messageOk'):
            try:
                portCom.write(dernierRelaiActiverPompe)
                time.sleep(1)
                nbCar = portCom.in_waiting
                retour = portCom.read(nbCar)
                with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiPompe.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write(dernierRelaiActiverPompe)
                    fichier.truncate()
                portCom.flushInput()
            except:
                portCom.flushInput()
    try:
        portCom.write('S')
        time.sleep(1)
        nbCar = portCom.in_waiting
        retour = portCom.read(nbCar)
        with open('/mnt/USB1/Growbox_Control/Variable/etatsRelais.txt', 'w') as fichier:
            fichier.seek(0)
            fichier.write(retour)
            fichier.truncate()
        portCom.flushInput()
    except (ValueError, TypeError, AttributeError):
        portCom.flushInput()
    portCom.flushInput()
def commande_arduino():
    with open('/mnt/USB1/Growbox_Control/Variable/intractionExtractionAir.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        dernierRelaiActiverIntracteurExtracteur = fichier.read(2)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/ventilateurTemperature.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        dernierRelaiActiverVentilateurTemperature = fichier.read(2)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/lampe.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        dernierRelaiActiverLampe = fichier.read(2)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/ventilateur.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        dernierRelaiActiverVentilateur = fichier.read(2)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/pompeEau.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        dernierRelaiActiverPompe = fichier.read(2)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiIntracteurExtracteur.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        numeroRelaiIntracteurExtracteur = fichier.read(2)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiVentilateurTemperature.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        numeroRelaiVentilateurTemperature = fichier.read(2)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiLampe.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        numeroRelaiLampe = fichier.read(2)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiVentilateur.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        numeroRelaiVentilateur = fichier.read(2)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiPompe.txt', 'r') as fichier:
        d = fichier.readlines()
        fichier.seek(0)
        numeroRelaiPompe = fichier.read(2)
        fichier.close()
    # Envoie des commandes
    if(dernierRelaiActiverIntracteurExtracteur != numeroRelaiIntracteurExtracteur):
        retour = ''
        while(retour != 'messageOk'):
            try:
                portCom.write(dernierRelaiActiverIntracteurExtracteur)
                numeroRelaiIntracteurExtracteur = dernierRelaiActiverIntracteurExtracteur
                time.sleep(1)
                nbCar = portCom.in_waiting
                retour = portCom.read(nbCar)
                with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiIntracteurExtracteur.txt','w') as fichier:
                    fichier.seek(0)
                    fichier.write(dernierRelaiActiverIntracteurExtracteur)
                    fichier.truncate()
                portCom.flushInput()
            except:
                portCom.flushInput()
    if(dernierRelaiActiverVentilateurTemperature != numeroRelaiVentilateurTemperature):
        retour = ''
        while(retour != 'messageOk'):
            try:
                portCom.write(dernierRelaiActiverVentilateurTemperature)
                numeroRelaiVentilateurTemperature = dernierRelaiActiverVentilateurTemperature
                time.sleep(1)
                nbCar = portCom.in_waiting
                retour = portCom.read(nbCar)
                with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiVentilateurTemperature.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write(dernierRelaiActiverVentilateurTemperature)
                    fichier.truncate()
                portCom.flushInput()
            except:
                portCom.flushInput()
    if(dernierRelaiActiverLampe != numeroRelaiLampe):
        retour = ''
        while(retour != 'messageOk'):
            try:
                portCom.write(dernierRelaiActiverLampe)
                numeroRelaiLampe = dernierRelaiActiverLampe
                time.sleep(1)
                nbCar = portCom.in_waiting
                retour = portCom.read(nbCar)
                with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiLampe.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write(dernierRelaiActiverLampe)
                    fichier.truncate()
                portCom.flushInput()
            except:
                portCom.flushInput()
    if(dernierRelaiActiverVentilateur != numeroRelaiVentilateur):
        retour = ''
        while(retour != 'messageOk'):
            try:
                portCom.write(dernierRelaiActiverVentilateur)
                numeroRelaiVentilateur = dernierRelaiActiverVentilateur
                time.sleep(1)
                nbCar = portCom.in_waiting
                retour = portCom.read(nbCar)
                with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiVentilateur.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write(dernierRelaiActiverVentilateur)
                    fichier.truncate()
                portCom.flushInput()
            except:
                portCom.flushInput()
    if(dernierRelaiActiverPompe != numeroRelaiPompe):
        retour = ''
        while(retour != 'messageOk'):
            try:
                portCom.write(dernierRelaiActiverPompe)
                numeroRelaiPompe = dernierRelaiActiverPompe
                time.sleep(1)
                nbCar = portCom.in_waiting
                retour = portCom.read(nbCar)
                with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiPompe.txt', 'w') as fichier:
                    fichier.seek(0)
                    fichier.write(dernierRelaiActiverPompe)
                    fichier.truncate()
                portCom.flushInput()
            except:
                portCom.flushInput()
    try:
        portCom.write('S')
        time.sleep(1)
        nbCar = portCom.in_waiting
        retour = portCom.read(nbCar)
        with open('/mnt/USB1/Growbox_Control/Variable/etatsRelais.txt', 'r') as fichier:
            d = fichier.readlines()
            fichier.seek(0)
            etatsRelais = fichier.read()
            fichier.close()
        if(retour != etatsRelais):
            with open('/mnt/USB1/Growbox_Control/Variable/etatsRelais.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write(retour)
                fichier.truncate()
            portCom.flushInput()
    except (ValueError, TypeError, AttributeError):
        portCom.flushInput()
    portCom.flushInput()
def reception_capteur_dht11():
    portCom.write('T')
    time.sleep(1)
    nbCar = portCom.in_waiting
    retour = portCom.read(nbCar)
    try:
        retour = int(retour)
    except (ValueError, TypeError, AttributeError):
        portCom.flushInput()
    if(retour >= 0 and retour <= 6000 and isinstance(retour,int) == True):
        try:
            retour = str(retour)
            with open('/mnt/USB1/Growbox_Control/Variable/temperatureHumidite.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write(retour)
                fichier.truncate()
        except (ValueError, TypeError, AttributeError):
            portCom.flushInput()
    portCom.flushInput()
def reception_capteur_humidite_terreau():
    portCom.write('U')
    time.sleep(1)
    nbCar = portCom.in_waiting
    retour = portCom.read(nbCar)
    try:
        retour = float(retour)
        retour = math.trunc(retour)
        retour = int(retour)
    except (ValueError, TypeError, AttributeError):
        portCom.flushInput()
    if(retour >= 0 and retour <= 1023 and isinstance(retour,int) == True):
        try:
            retour = str(retour)
            with open('/mnt/USB1/Growbox_Control/Variable/humiditeTerreau.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write(retour)
                fichier.truncate()
        except (ValueError, TypeError, AttributeError):
            portCom.flushInput()
    portCom.flushInput()
def reception_capteur_niveau_reservoir():
    portCom.write('V')
    time.sleep(1)
    nbCar = portCom.in_waiting
    retour = portCom.read(nbCar)
    try:
        retour = float(retour)
        retour = math.trunc(retour)
        retour = int(retour)
    except (ValueError, TypeError, AttributeError):
        portCom.flushInput()
    if(retour >= 0 and retour <= 1023 and isinstance(retour,int) == True):
        try:
            retour = str(retour)
            with open('/mnt/USB1/Growbox_Control/Variable/niveauReservoir.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write(retour)
                fichier.truncate()
        except (ValueError, TypeError, AttributeError):
            portCom.flushInput()
    portCom.flushInput()
def reception_capteur_luminosite():
    portCom.write('W')
    time.sleep(1)
    nbCar = portCom.in_waiting
    retour = portCom.read(nbCar)
    try:
        retour = float(retour)
        retour = math.trunc(retour)
        retour = int(retour)
    except (ValueError, TypeError, AttributeError):
        portCom.flushInput()
    if(retour >= 0 and retour <= 1023 and isinstance(retour,int) == True):
        try:
            retour = str(retour)
            with open('/mnt/USB1/Growbox_Control/Variable/luminosite.txt', 'w') as fichier:
                fichier.seek(0)
                fichier.write(retour)
                fichier.truncate()
        except (ValueError, TypeError, AttributeError):
            portCom.flushInput()
    portCom.flushInput()
# Programme principal
# initialisation du port série
portCom = serial.Serial()
portCom.port = '/dev/ttyACM0'
portCom.baudrate = 115200
firstLoop = 1
killer = GracefulKiller()
while not killer.kill_now:
    # Ouverture du port série
    open_portcom()
    time.sleep(3)
    if(portCom.is_open):
        commande_arduino_firstloop()
    while(portCom.is_open and not killer.kill_now):
        commande_arduino()
        reception_capteur_dht11()
        reception_capteur_humidite_terreau()
        reception_capteur_niveau_reservoir()
        reception_capteur_luminosite()
        time.sleep(3)
