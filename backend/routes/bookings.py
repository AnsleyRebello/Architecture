from flask import Blueprint, request, jsonify
from backend.services.booking_service import BookingService

bookings_bp = Blueprint("bookings", __name__)

@bookings_bp.route("/", methods=["POST"])
def create_booking():
    try:
        data = request.get_json()
        booking = BookingService.create_booking(
            user_name=data.get("user_name"),
            email=data.get("email"),
            phone=data.get("phone")
        )
        return jsonify(booking.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@bookings_bp.route("/", methods=["GET"])
def get_bookings():
    try:
        bookings = BookingService.get_all_bookings()
        result = [booking.to_dict() for booking in bookings]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@bookings_bp.route("/<int:id>", methods=["GET"])
def get_booking(id):
    try:
        booking = BookingService.get_booking_by_id(id)
        return jsonify(booking.to_dict()), 200
    except Exception as e:
        return jsonify({"error": f"Booking not found: {str(e)}"}), 404

@bookings_bp.route("/<int:id>", methods=["PUT"])
def update_booking(id):
    try:
        data = request.get_json()
        booking = BookingService.update_booking(id, **data)
        return jsonify(booking.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@bookings_bp.route("/<int:id>", methods=["DELETE"])
def delete_booking(id):
    try:
        BookingService.delete_booking(id)
        return jsonify({"message": "Booking deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
