#Module fonctions mathématiques
#Copyright Musso Guiot Schlegel
#Version 1.0

#from statistics
#covariance()
#correlation()
#variance()
#mean()
#from math
#sum()
from statistics import * 
from math import *

#En paramètre la liste des données d'un parking 
def moyenneParking(liste):
    return mean(liste)
    #Retourne la moyenne des données

#En paramètre la liste des données d'un parking
def varianceParking(liste):
    return variance(liste)
    #Retourne la variance de la liste

#En paramètre une liste(liste1) et une autre liste(liste2)
def covarianceParkings(liste1,liste2):
    return covariance(liste1,liste2)
    #Retourne la covariance de deux séries de données

#En paramètre la liste des données d'un parking
def ecartTypeParking(liste):
    return pstdev(liste)
    #Retourne l'écart-type de la série de données
    
#En paramètre le nombre de place libre(placeLibre) et le nombre de la capacité(placeTotal)
def pourcentage(placeLibre,placeTotal):
    return round(placeTotal-placeLibre/placeTotal)
    #placeTotal-placeLibre vaut la place occupé. placeOccupé sur placeTotal donne le pourcentage de remplissage. donc à 100 % il est plein
    #et à 0% il est vide. 
