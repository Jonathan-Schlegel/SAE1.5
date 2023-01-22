import csv

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