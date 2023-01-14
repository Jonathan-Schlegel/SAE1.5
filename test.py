import json
import requests

response=requests.get("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json")
#Transformation d'un format JSON en structure Python
data=json.loads(response.text)
"""print(data["data"])"""
#Obtenir la donnée par un "chemin" date[]
recherche=[element for element in data["data"]["stations"][0]["station_id"]]
print(recherche)
