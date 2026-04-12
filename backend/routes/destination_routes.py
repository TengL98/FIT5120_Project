from flask import Blueprint, request, jsonify
from services.destination_service import get_recommended_destination

destination_bp = Blueprint("destination_bp", __name__)


@destination_bp.route("/api/destination/recommend", methods=["GET"])
def recommend_destination():
    destination_type = request.args.get("type")
    user_lat = request.args.get("userLat")
    user_lng = request.args.get("userLng")

    if not destination_type or not user_lat or not user_lng:
        return jsonify({
            "error": "Missing required query parameters: type, userLat, userLng"
        }), 400

    try:
        user_lat = float(user_lat)
        user_lng = float(user_lng)
    except ValueError:
        return jsonify({
            "error": "userLat and userLng must be valid numbers"
        }), 400

    result, status_code = get_recommended_destination(
        destination_type.lower(),
        user_lat,
        user_lng
    )

    return jsonify(result), status_code