import requests
import numpy as np

def get_distance(api_key, origin, destination):
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": origin,
        "destinations": destination,
        "key": api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    try:
        distance = data["rows"][0]["elements"][0]["distance"]["text"]
        return distance
    except KeyError:
        return "Distance information not available."


api_key = "AIzaSyD6nu8-KekfyVLGxQEv3jAhqrHtJgDp_0I"
cities = [
{"name": "Beijing", "coordinates": "39.9042,116.4074"},
{"name": "Shanghai", "coordinates": "31.2304,121.4737"},
{"name": "Xi'an", "coordinates": "34.3416,108.9398"},
{"name": "Guilin", "coordinates": "25.2736,110.2900"},
{"name": "Chengdu", "coordinates": "30.5728,104.0668"},
{"name": "Hangzhou", "coordinates": "30.2741,120.1551"},
{"name": "Suzhou", "coordinates": "31.2989,120.5853"},
{"name": "Shenzhen", "coordinates": "22.5431,114.0579"},
{"name": "Guangzhou", "coordinates": "23.1291,113.2644"},
{"name": "Lhasa", "coordinates": "29.6536,91.1401"},
{"name": "Lijiang", "coordinates": "26.8550,100.2278"},
{"name": "Dali", "coordinates": "25.6065,100.2676"},
{"name": "Chongqing", "coordinates": "29.4316,106.9123"},
{"name": "Nanjing", "coordinates": "32.0603,118.7969"},
{"name": "Harbin", "coordinates": "45.8038,126.5340"}
]


temp = []
for city in cities:
    for other_city in cities:
        if city != other_city:
            origin = city["coordinates"]
            destination = other_city["coordinates"]
            distance = get_distance(api_key, origin, destination)
            #print(f"Distance from {city['name']} to {other_city['name']}: {distance}")
            temp.append(distance)
distance_matrix = np.array(temp).reshape(15,-1)
with open ('distance_matrix.txt', 'w') as f:
    f.write(str(distance_matrix))

