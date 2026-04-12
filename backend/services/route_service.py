import requests

OSRM_BASE_URL = "https://router.project-osrm.org"


def get_walking_route(start_lat, start_lng, end_lat, end_lng):
    url = (
        f"{OSRM_BASE_URL}/route/v1/walking/"
        f"{start_lng},{start_lat};{end_lng},{end_lat}"
    )

    params = {
        "overview": "full",
        "geometries": "geojson"
    }

    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()

    data = response.json()
    routes = data.get("routes", [])

    if not routes:
        return None

    geometry = routes[0].get("geometry", {})
    coordinates = geometry.get("coordinates", [])

    if not coordinates:
        return None

    return coordinates