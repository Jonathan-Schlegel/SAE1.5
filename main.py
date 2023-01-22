#Fichier exécution du programme principale
from recuperationStockageDonnee import *
from lectureDonneFichier import *
import time

#Liste des parkings voitures utilisé pour les liens et fichiers
parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']

#Fonction global pour récupérer et stocker les données
#Elle prend en paramètre(heure) l'intervale de temps pendant laquelle la récolte sera faite
#ainsi que la période d'échantillonnage(minute)
def lancement(heure,echantillonnage):
    #Boucle qui itère le bon nombre de fois car calcul du nombre d'échantillonnage 
    for x in range(round((heure*60)/echantillonnage)):
        #Récupération de l'instat 
        temps=int(time.time())
        #Boucle pour parser tous les parkings
        for parking in parkings:
            liste=recuperationParkingVoiture(parking,temps)
            ecritureDonneeVoiture(liste,parking)
        #On récupère toutes les stations en même temps
        liste=recuperationParkingVelo(temps)
        print(liste)
        #Et on stockent toutes les stations dans un même fichier
        ecritureDonneeVelo(liste)
        #On attend la période d'échantillonnage. Multiplié par 60 car paramètre en seconde 
        time.sleep(echantillonnage*60)

lancement(24,5)
"""donneeVelo=lectureDonneeVelo()"""




