import json
import requests
"""
reponse=requests.get("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_information.json")
data=json.loads(reponse.text)
#Dictionnaire où se trouvera les informations parsées
dicoStationId={}
#Dans le dictionnaire on associe la station_id avec name(key:stations_id,value:name)
for x in range(len(data["data"]["stations"])):
    dicoStationId[data["data"]["stations"][x]["station_id"]]=data["data"]["stations"][x]["name"]
print(dicoStationId)

#Ou en générateur(marche pas)
{dicoStationId[data["data"]["stations"][x]["station_id"]]=data["data"]["stations"][x]["name"] for x in range(len(data["data"]["stations"]))}
print(dicoStationId)
"""
listStationID={'001': 'Rue Jules Ferry - Gare Saint-Roch', '002': 'Comédie', '003': 'Esplanade', '004': 'Hôtel de Ville', '005': 'Corum', '006': 'Place Albert 1er - St Charles', '007': 'Foch', '008': 'Halles Castellane', '009': 'Observatoire', '010': 'Rondelet', '011': 'Plan Cabanes', '012': 'Boutonnet', '013': 'Emile Combes', '014': 'Beaux-Arts', '015': 'Les Aubes', '016': 'Antigone centre', '017': 'Médiathèque Emile Zola', '018': "Nombre d'Or", '019': 'Louis Blanc', '020': 'Gambetta', '021': 'Port Marianne', '022': 'Clemenceau', '023': 'Les Arceaux', '024': 'Cité Mion', '025': 'Nouveau Saint-Roch', '026': 'Renouvier', '027': 'Odysseum', '028': 'Saint-Denis', '029': 'Richter', '030': 'Charles Flahault', '031': 'Voltaire', '032': "Prés d'Arènes", '033': 'Garcia Lorca', '034': 'Vert Bois', '035': 'Malbosc', '036': 'Occitanie', '037': 'FacdesSciences', '038': 'Fac de Lettres', '039': 'Aiguelongue', '040': 'Jeu de Mail des Abbés', '041': 'Euromédecine', '042': 'Marie Caizergues', '043': 'Sabines', '044': 'Celleneuve', '045': 'Jardin de la Lironde', '046': 'Père Soulas', '047': 'Place Viala', '048': 'Hôtel du Département', '049': 'Tonnelles', '050': 'Parvis Jules Ferry - Gare Saint-Roch', '051': 'Pont de Lattes - Gare Saint-Roch', '053': 'Deux Ponts - Gare Saint-Roch', '054': 'Providence - Ovalie', '055': "Pérols Etang de l'Or", '056': 'Albert 1er - Cathédrale', '057': 'Saint-Guilhem - Courreau', '059': 'Sud De France'}

#Création liste par ordre alphabétique suite au changement de jeu de donnée
listeStationVelo=[]
for id,parking in listStationID.items():
    listeStationVelo.append(parking)
    listeStationVelo.sort()
print(listeStationVelo)
listeStationVelo=['Aiguelongue', 'Albert 1er - Cathédrale', 'Antigone centre', 'Beaux-Arts', 'Boutonnet', 'Celleneuve', 'Charles Flahault', 'Cité Mion', 'Clemenceau', 'Comédie', 'Corum', 'Deux Ponts - Gare Saint-Roch', 'Emile Combes', 'Esplanade', 'Euromédecine', 'Fac de Lettres', 'FacdesSciences', 'Foch', 'Gambetta', 'Garcia Lorca', 'Halles Castellane', 'Hôtel de Ville', 'Hôtel du Département', 'Jardin de la Lironde', 'Jeu de Mail des Abbés', 'Les Arceaux', 'Les Aubes', 'Louis Blanc', 'Malbosc', 'Marie Caizergues', 'Médiathèque Emile Zola', "Nombre d'Or", 'Nouveau Saint-Roch', 'Observatoire', 'Occitanie', 'Odysseum', 'Parvis Jules Ferry - Gare Saint-Roch', 'Place Albert 1er - St Charles', 'Place Viala', 'Plan Cabanes', 'Pont de Lattes - Gare Saint-Roch', 'Port Marianne', 'Providence - Ovalie', "Prés d'Arènes", 'Père Soulas', "Pérols Etang de l'Or", 'Renouvier', 'Richter', 'Rondelet', 'Rue Jules Ferry - Gare Saint-Roch', 'Sabines', 'Saint-Denis', 'Saint-Guilhem - Courreau', 'Sud De France', 'Tonnelles', 'Vert Bois', 'Voltaire']

    