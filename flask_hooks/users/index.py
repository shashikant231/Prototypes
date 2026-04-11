from flask import Blueprint, request, jsonify


users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.before_app_request
def before_users_request():
    print("User API hit")


@users_bp.route("/", methods=["post"])
def users():
    data = request.json
    return jsonify({"message": "User created", "data": data})
