import json
from utils.geo_utils import calculate_distance_meters

ROUTE_BUFFER_METERS = 150


def load_geojson(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_toilets():
    return load_geojson("data/public_toilets_clean.geojson")


def load_furniture():
    return load_geojson("data/street_furniture_clean.geojson")


def normalize_facility_name(facility_type, raw_name):
    if raw_name:
        return raw_name

    if facility_type == "bench":
        return "Bench nearby"
    if facility_type == "drinking_fountain":
        return "Drinking Fountain nearby"
    if facility_type == "toilet":
        return "Public Toilet nearby"

    return "Facility nearby"


def get_min_distance_to_route(lat, lng, route_points):
    min_distance = None

    for point in route_points:
        point_lng, point_lat = point
        distance = calculate_distance_meters(lat, lng, point_lat, point_lng)

        if min_distance is None or distance < min_distance:
            min_distance = distance

    return min_distance


def search_facilities_along_route(route_points):
    results = []

    toilets_data = load_toilets()
    for feature in toilets_data.get("features", []):
        props = feature.get("properties", {})
        geometry = feature.get("geometry", {})

        if geometry.get("type") != "Point":
            continue

        coords = geometry.get("coordinates", [])
        if len(coords) < 2:
            continue

        lng, lat = coords
        distance_to_route = get_min_distance_to_route(lat, lng, route_points)

        if distance_to_route is not None and distance_to_route <= ROUTE_BUFFER_METERS:
            results.append({
                "name": normalize_facility_name("toilet", props.get("name")),
                "type": "toilet",
                "lat": lat,
                "lng": lng,
                "distanceMeters": round(distance_to_route),
                "wheelchair": props.get("wheelchair"),
                "lastUpdated": None
            })

    furniture_data = load_furniture()
    for feature in furniture_data.get("features", []):
        props = feature.get("properties", {})
        geometry = feature.get("geometry", {})

        if geometry.get("type") != "Point":
            continue

        coords = geometry.get("coordinates", [])
        if len(coords) < 2:
            continue

        asset_type = props.get("asset_type", "")

        if asset_type == "Seat":
            facility_type = "bench"
        elif asset_type == "Drinking Fountain":
            facility_type = "drinking_fountain"
        else:
            continue

        lng, lat = coords
        distance_to_route = get_min_distance_to_route(lat, lng, route_points)

        if distance_to_route is not None and distance_to_route <= ROUTE_BUFFER_METERS:
            results.append({
                "name": normalize_facility_name(facility_type, props.get("location_desc")),
                "type": facility_type,
                "lat": lat,
                "lng": lng,
                "distanceMeters": round(distance_to_route),
                "conditionRating": props.get("condition_rating"),
                "lastUpdated": None
            })

    return sorted(results, key=lambda x: x["distanceMeters"])[:10]