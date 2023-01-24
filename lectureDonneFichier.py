import csv
#Notre prédécent code

"""
def lectureDonneeVelo():
    #Liste contenant les listes ajoutés au fur et à mesure des lignes
    listeVelo=[]
    with open('parkings/parkings_velo/velo.csv', 'r') as fichier:
        lecture = csv.reader(fichier , delimiter=',')
        #Par ligne on ajoute une liste 
        for row in (lecture):
            listeVelo.append(row)
        fichier.close()
    #Retour de la liste de liste
    return listeVelo
"""

def lectureDonneeVelo(parking):
    listeTemps=[]
    listePourcentage=[]
    with open(f"data/txt_file/velo/{parking}_time_occupation.txt") as fichier:
        lecture=fichier.readlines()
        for ligne in lecture:
            ligne=ligne.split()    
            listeTemps.append(ligne[1])
            listePourcentage.append(float(ligne[2]))
        fichier.close()
    return listeTemps,listePourcentage

def lectureDonneeVoiture(parking):
    listeTemps=[]
    listePourcentage=[]
    with open(f"data/txt_file/voiture/{parking}_time_occupation.txt") as fichier:
        lecture=fichier.readlines()
        for ligne in lecture:
            ligne=ligne.split()    
            listeTemps.append(ligne[1])
            listePourcentage.append(float(ligne[2]))
        fichier.close()
    return listeTemps,listePourcentage