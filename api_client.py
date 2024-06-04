# api_client.py
import requests

from config import API_KEY, API_URL

def send_data_to_server(data):
    headers = {'Authorization': f'Bearer {API_KEY}'}
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        if response.status_code == 200:
            print("Données envoyées avec succès")
        else:
            print(f"Erreur lors de l'envoi des données: {response.status_code}")
    except Exception as e:
        print(f"Erreur de connexion au serveur: {e}")
