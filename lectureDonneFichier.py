import csv

def lectureDonneeVelo():
    listeVelo=[]
    with open('parkings/parkings_velo/velo.csv', 'r') as fichier:
        lecture = csv.reader(fichier , delimiter=',')
        for row in (lecture):
            listeVelo.append(row)
        fichier.close()
    return listeVelo