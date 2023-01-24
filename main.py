#Fichier exécution du programme principale
from recuperationStockageDonnee import *
from lectureDonneFichier import *
import time
from mathematiques import *

#Liste des parkings voitures utilisé pour les liens et fichiers
voiture=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']
velo=['Aiguelongue', 'Albert 1er - Cathédrale', 'Antigone centre', 'Beaux-Arts', 'Boutonnet', 'Celleneuve', 'Charles Flahault', 'Cité Mion', 'Clemenceau', 'Comédie', 'Corum', 'Deux Ponts - Gare Saint-Roch', 'Emile Combes', 'Esplanade', 'Euromédecine', 'Fac de Lettres', 'FacdesSciences', 'Foch', 'Gambetta', 'Garcia Lorca', 'Halles Castellane', 'Hôtel de Ville', 'Hôtel du Département', 'Jardin de la Lironde', 'Jeu de Mail des Abbés', 'Les Arceaux', 'Les Aubes', 'Louis Blanc', 'Malbosc', 'Marie Caizergues', 'Médiathèque Emile Zola', "Nombre d_Or", 'Nouveau Saint-Roch', 'Observatoire', 'Occitanie', 'Odysseum', 'Parvis Jules Ferry - Gare Saint-Roch', 'Place Albert 1er - St Charles', 'Place Viala', 'Plan Cabanes', 'Pont de Lattes - Gare Saint-Roch', 'Port Marianne', 'Providence - Ovalie', "Prés d_Arènes", 'Père Soulas', "Pérols Etang de l_Or", 'Renouvier', 'Richter', 'Rondelet', 'Rue Jules Ferry - Gare Saint-Roch', 'Sabines', 'Saint-Denis', 'Saint-Guilhem - Courreau', 'Sud De France', 'Tonnelles', 'Voltaire']

#Fonction global pour récupérer et stocker les données
#Elle prend en paramètre(heure) l'intervale de temps pendant laquelle la récolte sera faite
#ainsi que la période d'échantillonnage(minute)
def lancement(heure,echantillonnage):
    #Boucle qui itère le bon nombre de fois car calcul du nombre d'échantillonnage 
    for x in range(round((heure*60)/echantillonnage)):
        #Récupération de l'instat 
        temps=int(time.time())
        #Boucle pour parser tous les parkings
        for parking in velo:
            liste=recuperationParkingVoiture(parking,temps)
            ecritureDonneeVoiture(liste,parking)
        #On récupère toutes les stations en même temps
        liste=recuperationParkingVelo(temps)
        print(liste)
        #Et on stockent toutes les stations dans un même fichier
        ecritureDonneeVelo(liste)
        #On attend la période d'échantillonnage. Multiplié par 60 car paramètre en seconde 
        time.sleep(echantillonnage*60)
"""        
maximum=[]
minimum=[]
moyenne=[]
for parking in velo:
    listeTemps,listePourcentage=lectureDonneeVelo(parking)
    print(listePourcentage)
"""
"""
#Moyenne
moyenne=[]
for parking in voiture:
    listeTemps,listePourcentage=lectureDonneeVoiture(parking)
    moyenne.append(mean(listePourcentage))
print(moyenne)
print(min(moyenne))
print(max(moyenne))
print(mean(moyenne))
"""
"""
#Creation des fichiers comptatible aux formats pour les graphiques
for parking in voiture:
    lectureEcritureFichier(parking)
"""
"""
x,listePourcentage=lectureDonneeVoiture("FR_MTP_ANTI")
y,listePourcentage1=lectureDonneeVelo("Aiguelongue")
"""
"""
#Covariance des parkings velo et voiture.
print(covarianceParkings(listePourcentage,listePourcentage1))

print (correlation(listePourcentage,listePourcentage1))

print (ecartTypeParking(listePourcentage))
"""
for parking in voiture:
    lectureEcritureFichier9(parking)
