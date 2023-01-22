#Module fonctions récupération de donnée pour stockage vers fichiers
import requests
from lxml import etree
import json
import time
import csv

#Dictionnaire station avec leur ID
listStationID={'001': 'Rue Jules Ferry - Gare Saint-Roch', '002': 'Comédie', '003': 'Esplanade', '004': 'Hôtel de Ville', '005': 'Corum', '006': 'Place Albert 1er - St Charles', '007': 'Foch', '008': 'Halles Castellane', '009': 'Observatoire', '010': 'Rondelet', '011': 'Plan Cabanes', '012': 'Boutonnet', '013': 'Emile Combes', '014': 'Beaux-Arts', '015': 'Les Aubes', '016': 'Antigone centre', '017': 'Médiathèque Emile Zola', '018': "Nombre d'Or", '019': 'Louis Blanc', '020': 'Gambetta', '021': 'Port Marianne', '022': 'Clemenceau', '023': 'Les Arceaux', '024': 'Cité Mion', '025': 'Nouveau Saint-Roch', '026': 'Renouvier', '027': 'Odysseum', '028': 'Saint-Denis', '029': 'Richter', '030': 'Charles Flahault', '031': 'Voltaire', '032': "Prés d'Arènes", '033': 'Garcia Lorca', '034': 'Vert Bois', '035': 'Malbosc', '036': 'Occitanie', '037': 'FacdesSciences', '038': 'Fac de Lettres', '039': 'Aiguelongue', '040': 'Jeu de Mail des Abbés', '041': 'Euromédecine', '042': 'Marie Caizergues', '043': 'Sabines', '044': 'Celleneuve', '045': 'Jardin de la Lironde', '046': 'Père Soulas', '047': 'Place Viala', '048': 'Hôtel du Département', '049': 'Tonnelles', '050': 'Parvis Jules Ferry - Gare Saint-Roch', '051': 'Pont de Lattes - Gare Saint-Roch', '053': 'Deux Ponts - Gare Saint-Roch', '054': 'Providence - Ovalie', '055': "Pérols Etang de l'Or", '056': 'Albert 1er - Cathédrale', '057': 'Saint-Guilhem - Courreau', '059': 'Sud De France'}


#Cette fonction n'a pour but que de recolter les données d'un parking mis en paramètre. 
def recuperationParkingVoiture(parking,temps):
        response=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{parking}.xml")
        #On stocke la page dans un fichier
        f=open("response.txt","w",encoding="utf8")
        f.write(response.text)
        f.close()
        #Ensuite on le parse
        tree= etree.parse("response.txt")
        #Récupération Place libre
        for user in tree.xpath("Free"):
            placeLibre=user.text
        #Récupération Place total
        for user in tree.xpath("Total"):
            placeTotal=user.text
        donnees=[temps,placeLibre,placeTotal]
        #Retourne une liste contant des strings du temps en seconde "epoch" mis en paramètre,
        #des places libres ainsi que les places totales
        return donnees


#Fonction récupérant les informations des stations vélomagg du site
def recuperationParkingVelo(temps):
    #Liste contenant les listes des différentes stations qui seront ajoutées  
    listeVelo=[]
    response=requests.get("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json")
    #Structure le fichier json en structure compréhensible par Python
    data=json.loads(response.text)
    for x in range(len(data["data"]["stations"])):
        #Récupération vélo disponible
        veloLibre=data["data"]["stations"][x]["num_bikes_available"]
        #Récupération vélo emprunté
        veloEmprunte=data["data"]["stations"][x]["num_docks_available"]
        #Ajout d'une liste dans la principale d'une station contenant ses vélo disponible 
        #et ses vélos empruntés
        listeVelo.append([veloLibre,veloEmprunte])
    #Ajout à la fin de la liste principale le temps de capture
    listeVelo.append(temps)
    return listeVelo
    #Retourne une liste de liste sous la forme [[veloLibre0,veloEmprunte0],[veloLibre1,veloEmprunte1]]


#Fonction qui prend en paramètre la liste de liste vélo
def ecritureDonneeVelo(liste):
    #Dans le fichier du dossier parkings on écrit au format csv la liste de liste 
    with open("parkings/parkings_velo/velo.csv","a",newline="") as fichier:
        ecriture= csv.writer(fichier,delimiter=",")
        #On l'écrit sur une ligne
        ecriture.writerow(liste)
        fichier.close()

#Fonction qui prend en paramètre le parking(pour le stocker dans le bon fichier) ainsi que 
#la liste avec ses valeurs
def ecritureDonneeVoiture(liste,parking):
    fichier=open(f"parkings/parkings_voiture/{parking}.csv","a",newline="")
    ecriture=csv.writer(fichier,delimiter=",")
    ecriture.writerow(liste)
    fichier.close()
