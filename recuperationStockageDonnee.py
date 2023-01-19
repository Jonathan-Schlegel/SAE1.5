#Module fonctions récupération de donnée pour stockage vers fichiers
import requests
from lxml import etree
import json
import time
import csv

#Liste station id
listStationID={'001': 'Rue Jules Ferry - Gare Saint-Roch', '002': 'Comédie', '003': 'Esplanade', '004': 'Hôtel de Ville', '005': 'Corum', '006': 'Place Albert 1er - St Charles', '007': 'Foch', '008': 'Halles Castellane', '009': 'Observatoire', '010': 'Rondelet', '011': 'Plan Cabanes', '012': 'Boutonnet', '013': 'Emile Combes', '014': 'Beaux-Arts', '015': 'Les Aubes', '016': 'Antigone centre', '017': 'Médiathèque Emile Zola', '018': "Nombre d'Or", '019': 'Louis Blanc', '020': 'Gambetta', '021': 'Port Marianne', '022': 'Clemenceau', '023': 'Les Arceaux', '024': 'Cité Mion', '025': 'Nouveau Saint-Roch', '026': 'Renouvier', '027': 'Odysseum', '028': 'Saint-Denis', '029': 'Richter', '030': 'Charles Flahault', '031': 'Voltaire', '032': "Prés d'Arènes", '033': 'Garcia Lorca', '034': 'Vert Bois', '035': 'Malbosc', '036': 'Occitanie', '037': 'FacdesSciences', '038': 'Fac de Lettres', '039': 'Aiguelongue', '040': 'Jeu de Mail des Abbés', '041': 'Euromédecine', '042': 'Marie Caizergues', '043': 'Sabines', '044': 'Celleneuve', '045': 'Jardin de la Lironde', '046': 'Père Soulas', '047': 'Place Viala', '048': 'Hôtel du Département', '049': 'Tonnelles', '050': 'Parvis Jules Ferry - Gare Saint-Roch', '051': 'Pont de Lattes - Gare Saint-Roch', '053': 'Deux Ponts - Gare Saint-Roch', '054': 'Providence - Ovalie', '055': "Pérols Etang de l'Or", '056': 'Albert 1er - Cathédrale', '057': 'Saint-Guilhem - Courreau', '059': 'Sud De France'}


#Cette fonction n'a pour but que de recolter les données d'un parkin mis en paramètre. 
def recuperationParkingVoiture(parking):
        response=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{parking}.xml")
        f=open("response.txt","w",encoding="utf8")
        f.write(response.text)
        f.close()
        tree= etree.parse("response.txt")
        #Place libre
        for user in tree.xpath("Free"):
            placeLibre=user.text
        #Place total
        for user in tree.xpath("Total"):
            placeTotal=user.text
        #On récupère le temps seconde epoch
        temps=time.time()
        donnees=[temps,placeLibre,placeTotal]
        #Retourne une liste contant des strings du temps en seconde "epoch", des places libres ainsi
        #que la place total
        return donnees


#Fonction récupérant les informations des stations vélomagg du site
def recuperationParkingVelo():
    #Liste contenant les listes des différentes stations qui seront ajoutées  
    listeDeListe=[]
    response=requests.get("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json")
    #Structure le fichier json en structure python
    data=json.loads(response.text)
    for x in range(len(data["data"]["stations"])):
        veloLibre=data["data"]["stations"][x]["num_bikes_available"]
        veloEmprunte=data["data"]["stations"][x]["num_docks_available"]
        #Ajout d'une liste d'une station contenant ses véldata["data"]["stations"][station]["num_bikes_available"]os disponibles et ses vélos empruntés
        listeDeListe.append([veloLibre,veloEmprunte])
    return listeDeListe
    #Retourne une liste de liste sous la forme [[veloLibre0,veloEmprunte0],[veloLibre1,veloEmprunte1]]


#Fonction qui prend en paramètre la liste de liste vélo ou voiture
def ecritureDonneeVelo(liste):
    #Dans le fichier du dossier parkings on écrit la liste de liste
    with open("parkings/velo.csv","a",newline="") as fichier:
        ecriture= csv.writer(fichier,delimiter=",")
        #On l'écrit sur une ligne
        ecriture.writerow(liste)
        fichier.close()


def ecritureDonneeVoiture(liste,parking):
    fichier=open(f"parkings/{parking}.csv","a",newline="")
    ecriture=csv.writer(fichier,delimiter=",")
    ecriture.writerow(liste)
    fichier.close()

recuperationParkingVoiture("FR_MTP_GARE")