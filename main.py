#Fichier exécution du programme principale
from recuperationStockageDonnee import *
import time

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']
"""'FR_MTP_ARCT',"""
def lancement(heure,echantillonnage):
    for x in range(round((heure*60)/echantillonnage)):
        print(x)
        for parking in parkings:
            liste=recuperationParkingVoiture(parking)
            ecritureDonneeVoiture(liste,parking)
            print(liste)
        liste=recuperationParkingVelo()
        print(liste)
        ecritureDonneeVelo(liste)
        time.sleep(echantillonnage*60)

lancement(24,0.5)


