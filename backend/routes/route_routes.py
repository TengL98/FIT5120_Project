from flask import Blueprint, request, jsonify
from services.destination_service import get_recommended_destination
from services.route_service import get_walking_route
from services.facility_service import search_facilities_along_route

route_bp = Blueprint("route_bp", __name__)


@route_bp.route("/api/route/plan", methods=["POST"])
def plan_route():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    destination_type = data.get("type")
    user_lat = data.get("userLat")
    user_lng = data.get("userLng")

    if destination_type is None or user_lat is None or user_lng is None:
        return (
            jsonify({"error": "Missing required fields: type, userLat, userLng"}),
            400,
        )

    try:
        user_lat = float(user_lat)
        user_lng = float(user_lng)
    except ValueError:
        return jsonify({"error": "userLat and userLng must be valid numbers"}), 400

    destination_result, destination_status = get_recommended_destination(
        destination_type.lower(), user_lat, user_lng
    )

    if destination_status != 200:
        return jsonify(destination_result), destination_status

    destination = destination_result.get("destination")

    if not destination:
        return jsonify(destination_result), 200

    try:
        route_points = get_walking_route(
            user_lat, user_lng, destination["lat"], destination["lng"]
        )
    except Exception:
        route_points = None

    if not route_points:
        return (
            jsonify(
                {
                    "destination": destination,
                    "route": [],
                    "facilities": [],
                    "message": "Route could not be generated",
                }
            ),
            200,
        )

    facilities = search_facilities_along_route(route_points)

    return (
        jsonify(
            {
                "destination": destination,
                "route": route_points,
                "facilities": facilities,
            }
        ),
        200,
    )
