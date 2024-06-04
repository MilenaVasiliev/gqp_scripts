# main.py
import time

from sensors import fetch_all_sensors_data
from data_processing import process_data, plot_data
from api_client import send_data_to_server

def main():
    while True:
        sensor_data = fetch_all_sensors_data()
        if sensor_data:
            processed_data = process_data(sensor_data)
            plot_data(processed_data)
            send_data_to_server(sensor_data)
        time.sleep(60)

if __name__ == "__main__":
    main()
