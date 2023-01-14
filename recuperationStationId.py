import json
import requests

reponse=requests.get("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_information.json")
data=json.loads(reponse.text)
#Dictionnaire où se trouvera les informations parsées
dicoStationId={}
#Dans le dictionnaire on associe la station_id avec name(key:stations_id,value:name)
for x in range(len(data["data"]["stations"])):
    dicoStationId[data["data"]["stations"][x]["station_id"]]=data["data"]["stations"][x]["name"]
print(dicoStationId)

#Ou en générateur(marche pas)
"""{dicoStationId[data["data"]["stations"][x]["station_id"]]=data["data"]["stations"][x]["name"] for x in range(len(data["data"]["stations"]))}
print(dicoStationId)"""

    