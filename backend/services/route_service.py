import os
import requests

ORS_API_KEY = os.environ.get("ORS_API_KEY", "")
ORS_BASE_URL = "https://api.openrouteservice.org/v2/directions/foot-walking/geojson"


def get_walking_route(start_lat, start_lng, end_lat, end_lng):
    headers = {"Authorization": ORS_API_KEY, "Content-Type": "application/json"}
    body = {"coordinates": [[start_lng, start_lat], [end_lng, end_lat]]}

    response = requests.post(ORS_BASE_URL, json=body, headers=headers, timeout=20)
    response.raise_for_status()

    data = response.json()
    features = data.get("features", [])

    if not features:
        return None

    coordinates = features[0].get("geometry", {}).get("coordinates", [])

    if not coordinates:
        return None

    return coordinates
