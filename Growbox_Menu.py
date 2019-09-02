#!/usr/bin/python
# coding: utf8

import time
import signal
import os
import subprocess
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
def affiche_menu():
    os.system('cls||clear') # effacer l'écran
    commande = raw_input('\n0 - Contrôles\n'
                         '1 - Réglages\n'
                         'q - Exit\n'
                         '\nEntrez le n° du menu de votre choix : ')
    if(commande == '0'):
        controle()
    elif(commande == '1'):
        reglage()
    elif(commande == 'q'):
        exit()
    else:
        affiche_menu()
def controle():
    nombreDeBoucleMax = 10
    while not killer.kill_now:
        os.system('cls||clear')
        with open('/mnt/USB1/Growbox_Control/Variable/etatsRelais.txt', 'r') as fichier:
            d = fichier.readlines()
            fichier.seek(0)
            etatsRelais = fichier.read()
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiIntracteurExtracteur.txt', 'r') as fichier:
            d = fichier.readlines()
            fichier.seek(0)
            intracteurExtracteur = fichier.read(2)
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiVentilateurTemperature.txt', 'r') as fichier:
            d = fichier.readlines()
            fichier.seek(0)
            ventilateurTemperature = fichier.read(2)
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiLampe.txt', 'r') as fichier:
            d = fichier.readlines()
            fichier.seek(0)
            lampe = fichier.read(2)
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiVentilateur.txt', 'r') as fichier:
            d = fichier.readlines()
            fichier.seek(0)
            ventilateur = fichier.read(2)
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Variable/numeroRelaiPompe.txt', 'r') as fichier:
            d = fichier.readlines()
            fichier.seek(0)
            pompe = fichier.read(2)
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Variable/niveauBasReservoir.txt', 'r') as fichier:
            d = fichier.readlines()
            fichier.seek(0)
            niveauBasReservoir = fichier.read()
            fichier.close()
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
        with open('/mnt/USB1/Growbox_Control/Variable/luminosite.txt', 'r') as fichier:
            d = fichier.readlines()
            fichier.seek(0)
            luminosite = fichier.read()
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Variable/etatAmpoule.txt', 'r') as fichier:
            d = fichier.readlines()
            fichier.seek(0)
            etatAmpoule = fichier.read()
            fichier.close()
        print('Relais actifs : %s') % etatsRelais
        print('Intracteur : %s') % intracteurExtracteur
        print('VentilateurTemp : %s') % ventilateurTemperature
        print('Lampe : %s') % lampe
        print('Ventilateur : %s') % ventilateur
        print('Pompe : %s') % pompe
        print('Capteur photosensible : %s') % luminosite
        print('Température et humidité : température : %s, humidité : %s') % (temperature, humidite)
        print('Niveau Réservoir : %s') % niveauBasReservoir
        print('Etat lampe : %s') % etatAmpoule
        nombreDeBoucleMax = nombreDeBoucleMax - 1
        time.sleep(4)
        if(nombreDeBoucleMax == 0):
            affiche_menu()
        else:
            affiche_menu()
def reglage():
    os.system('cls||clear')
    commande = raw_input('\n0 - Mode croissance\n'
                         '1 - Mode floraison\n'
                         '2 - Changer les horaires de fonctionnement\n'
                         'q - Retour au menu principal\n'
                         '\nEntrez le n° du réglage que vous souhaitez effectuer : ')
    if(commande == '0'):
        passer_en_cro()
    elif(commande == '1'):
        passer_en_flo()
    elif(commande == '2'):
        changer_les_horaires()
    else:
        affiche_menu()
def passer_en_flo():
    os.system('cls||clear')
    listeFichier  = os.listdir('/mnt/USB1/Growbox_Control/')
    for i in range(len(listeFichier)):
        if(listeFichier[i] == 'Growbox_Time_Event_Flo.py'):
           fichier = 'pasEnFlo'
        elif(listeFichier[i] == 'Growbox_Time_Event_Cro.py'):
           fichier = 'enFlo'
    if(fichier == 'pasEnFlo'):
        os.rename('/mnt/USB1/Growbox_Control/Growbox_Time_Event.py', '/mnt/USB1/Growbox_Control/Growbox_Time_Event_Cro.py')
        os.rename('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Flo.py', '/mnt/USB1/Growbox_Control/Growbox_Time_Event.py')
        ouputGrowboxTimeEvent = subprocess.Popen(['pgrep', '-f', '/usr/bin/python /mnt/USB1/Growbox_Control/Growbox_Time_Event.py'], stdout=subprocess.PIPE)
        pidGrowboxTimeEvent = ouputGrowboxTimeEvent.stdout.read()
        os.kill(int(pidGrowboxTimeEvent), signal.SIGINT)
        print('Vous venez de passer en floraison!')
        time.sleep(3)
    elif(fichier == 'enFlo'):
        print('Déjà en floraison!')
        time.sleep(3)
    else:
        print('Fichier Manquant Growbox_Time_Event_Cro.py ou Growbox_Time_Event_Flo.py dans le dossier /mnt/USB1/Growbox_Control/')
        time.sleep(3)
        affiche_menu()
    affiche_menu()
def passer_en_cro():
    os.system('cls||clear')
    listeFichier  = os.listdir('/mnt/USB1/Growbox_Control/')
    for i in range(len(listeFichier)):
        if(listeFichier[i] == 'Growbox_Time_Event_Cro.py'):
           fichier = 'pasEnCro'
        elif(listeFichier[i] == 'Growbox_Time_Event_Flo.py'):
           fichier = 'enCro'
    if(fichier == 'pasEnCro'):
        os.rename('/mnt/USB1/Growbox_Control/Growbox_Time_Event.py', '/mnt/USB1/Growbox_Control/Growbox_Time_Event_Flo.py')
        os.rename('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Cro.py', '/mnt/USB1/Growbox_Control/Growbox_Time_Event.py')
        ouputGrowboxTimeEvent = subprocess.Popen(['pgrep', '-f', '/usr/bin/python /mnt/USB1/Growbox_Control/Growbox_Time_Event.py'], stdout=subprocess.PIPE)
        pidGrowboxTimeEvent = ouputGrowboxTimeEvent.stdout.read()
        os.kill(int(pidGrowboxTimeEvent), signal.SIGINT)
        print('Vous venez de passer en croissance')
        time.sleep(3)
    elif(fichier == 'enCro'):
        print('Déjà en croissance!')
        time.sleep(3)
    else:
        print('Fichier Manquant Growbox_Time_Event_Cro.py ou Growbox_Time_Event_Flo.py dans le dossier /mnt/USB1/Growbox_Control/')
        time.sleep(3)
        affiche_menu()
    affiche_menu()
def changer_les_horaires():
    os.system('cls||clear')
    print('Les heures sont de 0h à 23h')
    heureDemarrageCro = raw_input('Heure de début de fonctionnement de la lampe et du ventilateur (croissance) : ')
    heureDemarrageCroInt = int(heureDemarrageCro)
    if(heureDemarrageCroInt < 0 or heureDemarrageCroInt > 23):
        changer_les_horaires()
    heureDemarrageCro = 'todayCroStart = dateNow.replace(hour=%s, minute=0, second=0, microsecond=0)' % heureDemarrageCro
    heureArretCro = raw_input('Heure de fin de fonctionnement de la lampe et du ventilateur (croissance) : ')
    heureArretCroInt = int(heureArretCro)
    if(heureArretCroInt < 0 or heureArretCroInt > 23):
        changer_les_horaires()
    heureArretCro = 'todayCroEnd = dateNow.replace(hour=%s, minute=0, second=0, microsecond=0)' % heureArretCro
    heureDemarrageFlo = raw_input('Heure de début de fonctionnement de la lampe et du ventilateur (floraison) : ')
    heureDemarrageFloInt = int(heureDemarrageFlo)
    if(heureDemarrageFloInt < 0 or heureDemarrageFloInt > 23):
        changer_les_horaires()
    heureDemarrageFlo = 'todayFloStart = dateNow.replace(hour=%s, minute=0, second=0, microsecond=0)' % heureDemarrageFlo
    heureArretFlo = raw_input('Heure de fin de fonctionnement de la lampe et du ventilateur (floraison) : ')
    heureArretFloInt = int(heureArretFlo)
    if(heureArretFloInt < 0 or heureArretFloInt > 23):
        changer_les_horaires()
    heureArretFlo = 'todayFloEnd = dateNow.replace(hour=%s, minute=0, second=0, microsecond=0)' % heureArretFlo
    with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event.py','r') as fichier:
        listeLigne = fichier.readlines()
        for i in range(len(listeLigne)):
            if 'todayCroStart = dateNow.replace' in listeLigne[i]:
                chaineTrouver = listeLigne[i]
        chaineTrouver = chaineTrouver.rstrip()
        chaineTrouver = chaineTrouver.strip()
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event.py','r') as fichier:
        chaineRemplace = fichier.read().replace(str(chaineTrouver), str(heureDemarrageCro))
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event.py','w') as fichier:
        fichier.write(chaineRemplace)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event.py','r') as fichier:
        listeLigne = fichier.readlines()
        for i in range(len(listeLigne)):
            if 'todayCroEnd = dateNow.replace' in listeLigne[i]:
                chaineTrouver = listeLigne[i]
        chaineTrouver = chaineTrouver.rstrip()
        chaineTrouver = chaineTrouver.strip()
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event.py','r') as fichier:
        chaineRemplace = fichier.read().replace(str(chaineTrouver), str(heureArretCro))
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event.py','w') as fichier:
        fichier.write(chaineRemplace)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event.py','r') as fichier:
        listeLigne = fichier.readlines()
        for i in range(len(listeLigne)):
            if 'todayFloStart = dateNow.replace' in listeLigne[i]:
                chaineTrouver = listeLigne[i]
        chaineTrouver = chaineTrouver.rstrip()
        chaineTrouver = chaineTrouver.strip()
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event.py','r') as fichier:
        chaineRemplace = fichier.read().replace(str(chaineTrouver), str(heureDemarrageFlo))
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event.py','w') as fichier:
        fichier.write(chaineRemplace)
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event.py','r') as fichier:
        listeLigne = fichier.readlines()
        for i in range(len(listeLigne)):
            if 'todayFloEnd = dateNow.replace' in listeLigne[i]:
                chaineTrouver = listeLigne[i]
        chaineTrouver = chaineTrouver.rstrip()
        chaineTrouver = chaineTrouver.strip()
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event.py','r') as fichier:
        chaineRemplace = fichier.read().replace(str(chaineTrouver), str(heureArretFlo))
        fichier.close()
    with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event.py','w') as fichier:
        fichier.write(chaineRemplace)
        fichier.close()
    listeFichier  = os.listdir('/mnt/USB1/Growbox_Control/')
    for i in range(len(listeFichier)):
        if(listeFichier[i] == 'Growbox_Time_Event_Cro.py'):
           fichierPresent = 'Growbox_Time_Event_Cro.py'
        elif(listeFichier[i] == 'Growbox_Time_Event_Flo.py'):
           fichierPresent = 'Growbox_Time_Event_Flo.py'
    if(fichierPresent == 'Growbox_Time_Event_Cro.py'):
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Cro.py','r') as fichier:
            listeLigne = fichier.readlines()
            for i in range(len(listeLigne)):
                if 'todayCroStart = dateNow.replace' in listeLigne[i]:
                    chaineTrouver = listeLigne[i]
            chaineTrouver = chaineTrouver.rstrip()
            chaineTrouver = chaineTrouver.strip()
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Cro.py','r') as fichier:
            chaineRemplace = fichier.read().replace(str(chaineTrouver), str(heureDemarrageCro))
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Cro.py','w') as fichier:
            fichier.write(chaineRemplace)
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Cro.py', 'r') as fichier:
            listeLigne = fichier.readlines()
            for i in range(len(listeLigne)):
                if 'todayCroEnd = dateNow.replace' in listeLigne[i]:
                    chaineTrouver = listeLigne[i]
            chaineTrouver = chaineTrouver.rstrip()
            chaineTrouver = chaineTrouver.strip()
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Cro.py','r') as fichier:
            chaineRemplace = fichier.read().replace(str(chaineTrouver), str(heureArretCro))
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Cro.py','w') as fichier:
            fichier.write(chaineRemplace)
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Cro.py','r') as fichier:
            listeLigne = fichier.readlines()
            for i in range(len(listeLigne)):
                if 'todayFloStart = dateNow.replace' in listeLigne[i]:
                    chaineTrouver = listeLigne[i]
            chaineTrouver = chaineTrouver.rstrip()
            chaineTrouver = chaineTrouver.strip()
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Cro.py','r') as fichier:
            chaineRemplace = fichier.read().replace(str(chaineTrouver), str(heureDemarrageFlo))
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Cro.py','w') as fichier:
            fichier.write(chaineRemplace)
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Cro.py','r') as fichier:
            listeLigne = fichier.readlines()
            for i in range(len(listeLigne)):
                if 'todayFloEnd = dateNow.replace' in listeLigne[i]:
                    chaineTrouver = listeLigne[i]
            chaineTrouver = chaineTrouver.rstrip()
            chaineTrouver = chaineTrouver.strip()
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Cro.py','r') as fichier:
            chaineRemplace = fichier.read().replace(str(chaineTrouver), str(heureArretFlo))
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Cro.py','w') as fichier:
            fichier.write(chaineRemplace)
            fichier.close()
        ouputGrowboxTimeEvent = subprocess.Popen(['pgrep', '-f', '/usr/bin/python /mnt/USB1/Growbox_Control/Growbox_Time_Event.py'], stdout=subprocess.PIPE)
        pidGrowboxTimeEvent = ouputGrowboxTimeEvent.stdout.read()
        os.kill(int(pidGrowboxTimeEvent), signal.SIGINT)
        print('Les horaires ont bien été modifiés.\n'
              'Vous êtes en floraison.')
        time.sleep(3)
        affiche_menu()
    elif(fichierPresent == 'Growbox_Time_Event_Flo.py'):
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Flo.py','r') as fichier:
            listeLigne = fichier.readlines()
            for i in range(len(listeLigne)):
                if 'todayCroStart = dateNow.replace' in listeLigne[i]:
                    chaineTrouver = listeLigne[i]
            chaineTrouver = chaineTrouver.rstrip()
            chaineTrouver = chaineTrouver.strip()
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Flo.py','r') as fichier:
            chaineRemplace = fichier.read().replace(str(chaineTrouver), str(heureDemarrageCro))
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Flo.py','w') as fichier:
            fichier.write(chaineRemplace)
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Flo.py','r') as fichier:
            listeLigne = fichier.readlines()
            for i in range(len(listeLigne)):
                if 'todayCroEnd = dateNow.replace' in listeLigne[i]:
                    chaineTrouver = listeLigne[i]
            chaineTrouver = chaineTrouver.rstrip()
            chaineTrouver = chaineTrouver.strip()
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Flo.py','r') as fichier:
            chaineRemplace = fichier.read().replace(str(chaineTrouver), str(heureArretCro))
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Flo.py','w') as fichier:
            fichier.write(chaineRemplace)
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Flo.py','r') as fichier:
            listeLigne = fichier.readlines()
            for i in range(len(listeLigne)):
                if 'todayFloStart = dateNow.replace' in listeLigne[i]:
                    chaineTrouver = listeLigne[i]
            chaineTrouver = chaineTrouver.rstrip()
            chaineTrouver = chaineTrouver.strip()
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Flo.py','r') as fichier:
            chaineRemplace = fichier.read().replace(str(chaineTrouver), str(heureDemarrageFlo))
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Flo.py','w') as fichier:
            fichier.write(chaineRemplace)
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Flo.py','r') as fichier:
            listeLigne = fichier.readlines()
            for i in range(len(listeLigne)):
                if 'todayFloEnd = dateNow.replace' in listeLigne[i]:
                    chaineTrouver = listeLigne[i]
            chaineTrouver = chaineTrouver.rstrip()
            chaineTrouver = chaineTrouver.strip()
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Flo.py','r') as fichier:
            chaineRemplace = fichier.read().replace(str(chaineTrouver), str(heureArretFlo))
            fichier.close()
        with open('/mnt/USB1/Growbox_Control/Growbox_Time_Event_Flo.py','w') as fichier:
            fichier.write(chaineRemplace)
            fichier.close()
        ouputGrowboxTimeEvent = subprocess.Popen(['pgrep', '-f', '/usr/bin/python /mnt/USB1/Growbox_Control/Growbox_Time_Event.py'], stdout=subprocess.PIPE)
        pidGrowboxTimeEvent = ouputGrowboxTimeEvent.stdout.read()
        os.kill(int(pidGrowboxTimeEvent), signal.SIGINT)
        print('Les horaires ont bien été modifiés.\n'
              'Vous êtes en croissance')
        time.sleep(3)
        affiche_menu()
    else:
        print('Fichier manquant Growbox_Time_Event_Cro.py ou Growbox_Time_Event_Flo.py dans le dossier /mnt/USB1/Growbox_Control/')
        time.sleep(3)
        affiche_menu()
# Programme
killer = GracefulKiller()
while not killer.kill_now:
    affiche_menu()
