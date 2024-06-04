# sensors.py
import requests

from config import SENSOR_IPS

def get_sensor_data(ip):
    try:
        response = requests.get(f"http://{ip}/data")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erreur lors de la récupération des données depuis {ip}")
            return None
    except Exception as e:
        print(f"Erreur de connexion au capteur {ip}: {e}")
        return None

def fetch_all_sensors_data():
    data = []
    for ip in SENSOR_IPS:
        sensor_data = get_sensor_data(ip)
        if sensor_data:
            data.append(sensor_data)
    return data
