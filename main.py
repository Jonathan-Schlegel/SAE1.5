from recuperationStockageDonnee import *

parking="FR_MTP_GARE"

liste=recuperationParkingVelo()
ecritureDonneeVelo(liste)
liste=recuperationParkingVoiture(parking)
ecritureDonneeVoiture(liste,parking)
