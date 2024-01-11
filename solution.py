import pandas as pd
from typing import Set
import requests
import sqlite3
import json

def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
    data = pd.read_csv(url, sep=';')
    
    
    columns_to_drop = ['Race', 'Count', 'Number of Veterans']
    data = data.drop(columns_to_drop, axis=1, errors='ignore')
    

    conn = sqlite3.connect('datos_demograficos.db')
    data.to_sql('demografia', conn, index=False, if_exists='replace')
    conn.close()

    return data

def ej_2_cargar_calidad_aire(ciudades: Set[str], api_key: str) -> None:
    calidad_aire = {'city': [], 'CO': [], 'NO2': [], 'O3': [], 'SO2': [], 'PM2.5': [], 'PM10': [], 'overall_aqi': []}

    for ciudad in ciudades:
        api_url = f'https://api.api-ninjas.com/v1/airquality?city={ciudad}'
        headers = {'X-Api-Key': api_key}
        response = requests.get(api_url, headers=headers)

        try:
            data = response.json()
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON for city {ciudad}: {e}")
            print(f"Response content: {response.text}")
            continue

        calidad_aire['city'].append(ciudad)
        calidad_aire['CO'].append(data.get('CO', {}).get('concentration', None))
        calidad_aire['NO2'].append(data.get('NO2', {}).get('concentration', None))
        calidad_aire['O3'].append(data.get('O3', {}).get('concentration', None))
        calidad_aire['SO2'].append(data.get('SO2', {}).get('concentration', None))
        calidad_aire['PM2.5'].append(data.get('PM2.5', {}).get('concentration', None))
        calidad_aire['PM10'].append(data.get('PM10', {}).get('concentration', None))
        calidad_aire['overall_aqi'].append(data.get('overall_aqi', None))

    calidad_aire_df = pd.DataFrame(calidad_aire)
    calidad_aire_df.to_csv('ciudades.csv', index=False)

    return data

def ej_2_cargar_calidad_aire(ciudades: Set[str], api_key: str) -> None:
    calidad_aire = {'city': [], 'CO': [], 'NO2': [], 'O3': [], 'SO2': [], 'PM2.5': [], 'PM10': [], 'overall_aqi': []}

    for ciudad in ciudades:
        api_url = f'https://api.api-ninjas.com/v1/airquality?city={ciudad}'
        headers = {'X-Api-Key': api_key}
        response = requests.get(api_url, headers=headers)

        try:
            data = response.json()
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON for city {ciudad}: {e}")
            print(f"Response content: {response.text}")
            continue

        calidad_aire['city'].append(ciudad)
        calidad_aire['CO'].append(data.get('CO', {}).get('concentration', None))
        calidad_aire['NO2'].append(data.get('NO2', {}).get('concentration', None))
        calidad_aire['O3'].append(data.get('O3', {}).get('concentration', None))
        calidad_aire['SO2'].append(data.get('SO2', {}).get('concentration', None))
        calidad_aire['PM2.5'].append(data.get('PM2.5', {}).get('concentration', None))
        calidad_aire['PM10'].append(data.get('PM10', {}).get('concentration', None))
        calidad_aire['overall_aqi'].append(data.get('overall_aqi', None))

    calidad_aire_df = pd.DataFrame(calidad_aire)
    calidad_aire_df.to_csv('ciudades.csv', index=False)