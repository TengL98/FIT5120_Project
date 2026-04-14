import requests
from utils.geo_utils import calculate_distance_meters

OVERPASS_URLS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
]

VALID_DESTINATION_TYPES = {
    "pharmacy": ("amenity", "pharmacy"),
    "grocery": ("shop", "supermarket"),
    "clinic": ("amenity", "clinic"),
    "garden": ("leisure", "park"),
    "cafe": ("amenity", "cafe"),
}

RADIUS_STEPS = {
    "pharmacy": [800, 1000],
    "grocery": [800, 1000],
    "clinic": [800, 1000],
    "garden": [1000],
    "cafe": [500, 800, 1000],
}


def build_overpass_query(osm_key, osm_value, lat, lng, radius):
    return f"""
    [out:json][timeout:20];
    (
      node["{osm_key}"="{osm_value}"](around:{radius},{lat},{lng});
      way["{osm_key}"="{osm_value}"](around:{radius},{lat},{lng});
    );
    out center;
    """


def fallback_name(destination_type):
    if destination_type == "pharmacy":
        return "Nearby Pharmacy"
    if destination_type == "grocery":
        return "Nearby Supermarket"
    if destination_type == "clinic":
        return "Nearby Clinic"
    if destination_type == "garden":
        return "Nearby Park"
    if destination_type == "cafe":
        return "Nearby Cafe"
    return "Nearby Destination"


def search_destinations_from_overpass(destination_type, user_lat, user_lng):
    osm_key, osm_value = VALID_DESTINATION_TYPES[destination_type]
    radius_list = RADIUS_STEPS.get(destination_type, [1000])

    for radius in radius_list:
        query = build_overpass_query(osm_key, osm_value, user_lat, user_lng, radius)

        response = None
        for overpass_url in OVERPASS_URLS:
            try:
                response = requests.get(
                    overpass_url, params={"data": query}, timeout=20
                )
                response.raise_for_status()
                break
            except requests.RequestException:
                response = None
                continue

        if response is None:
            continue

        data = response.json()
        results = []

        for element in data.get("elements", []):
            tags = element.get("tags", {})

            # nodes have lat/lon directly; ways have a "center" object after "out center;"
            if "lat" in element and "lon" in element:
                lat = element["lat"]
                lng = element["lon"]
            elif "center" in element:
                lat = element["center"]["lat"]
                lng = element["center"]["lon"]
            else:
                continue

            distance = calculate_distance_meters(user_lat, user_lng, lat, lng)
            real_name = tags.get("name") or tags.get("brand") or tags.get("operator")

            results.append(
                {
                    "name": real_name,
                    "type": destination_type,
                    "lat": lat,
                    "lng": lng,
                    "distanceMeters": round(distance),
                }
            )

        if results:
            return results

    return []


def get_recommended_destination(destination_type, user_lat, user_lng):
    if destination_type not in VALID_DESTINATION_TYPES:
        return {
            "error": "Invalid destination type. Supported types: pharmacy, grocery, clinic, garden, cafe"
        }, 400

    results = search_destinations_from_overpass(destination_type, user_lat, user_lng)

    if not results:
        return {
            "destination": None,
            "message": f"No nearby {destination_type} found within a 15-minute walk",
        }, 200

    named = [d for d in results if d["name"]]
    unnamed = [d for d in results if not d["name"]]

    candidates = named if named else unnamed
    recommended = min(candidates, key=lambda d: d["distanceMeters"])

    if not recommended["name"]:
        recommended["name"] = fallback_name(destination_type)

    return {"destination": recommended}, 200
