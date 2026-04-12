from flask import Blueprint, request, jsonify
from services.facility_service import search_facilities

facility_bp = Blueprint("facility_bp", __name__)


@facility_bp.route("/api/facilities", methods=["GET"])
def get_facilities():
    user_lat = request.args.get("userLat")
    user_lng = request.args.get("userLng")

    if not user_lat or not user_lng:
        return jsonify({
            "error": "Missing required query parameters: userLat, userLng"
        }), 400

    try:
        user_lat = float(user_lat)
        user_lng = float(user_lng)
    except ValueError:
        return jsonify({
            "error": "userLat and userLng must be valid numbers"
        }), 400

    facilities = search_facilities(user_lat, user_lng)

    if not facilities:
        return jsonify({
            "facilities": [],
            "message": "No rest stops available within a 15-minute walk"
        }), 200

    return jsonify({
        "facilities": facilities
    }), 200