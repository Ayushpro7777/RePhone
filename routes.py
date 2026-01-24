from flask import Blueprint, request, jsonify
from database import get_connection

api = Blueprint("api", __name__)

@api.route("/api/phones", methods=["GET"])
def get_phones():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phones ORDER BY id DESC")
    phones = cursor.fetchall()
    conn.close()

    return jsonify([dict(row) for row in phones])


@api.route("/api/phones/sell", methods=["POST"])
def sell_phone():
    data = request.get_json()

    name = data.get("name")
    price = data.get("price")
    image = data.get("image")

    if not name or not price:
        return jsonify({"error": "Name and price required"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO phones (name, price, image) VALUES (?, ?, ?)",
        (name, price, image)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Phone added successfully"}), 201
