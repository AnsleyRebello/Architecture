from flask import Blueprint, request, jsonify
from backend.models import db, User
from datetime import datetime

users_bp = Blueprint("users", __name__)

# Create User
@users_bp.route("/", methods=["POST"])  # /user/login
def create_user():
    data = request.get_json()
    user = User(
        username=data["username"],
        email=data["email"],
        password=data["password"],
        date_joined=datetime.utcnow()
    )
    db.session.add(user)
    db.session.commit()
    return {"response": "User created successfully"}, 201

# Get All Users
@users_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    result = [{"username": u.username, "email": u.email} for u in users]
    return jsonify(result)
