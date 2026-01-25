from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# MongoDB Connection
MONGO_URI = "mongodb+srv://rephoneuser:rephone123@cluster0.33tqcj2.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URI)

db = client["rephone"]
phones_collection = db["phones"]

# Test route
@app.route("/")
def home():
    return "RePhone Backend Running"

# Get all phones
@app.route("/api/phones", methods=["GET"])
def get_phones():
    phones = list(phones_collection.find({}, {"_id": 0}))
    return jsonify(phones)

# Sell phone (Add new phone)
@app.route("/api/phones/sell", methods=["POST"])
def sell_phone():
    data = request.json

    name = data.get("name")
    price = data.get("price")
    image = data.get("image")

    if not name or not price:
        return jsonify({"error": "Missing fields"}), 400

    phone = {
        "name": name,
        "price": price,
        "image": image or "https://via.placeholder.com/150"
    }

    phones_collection.insert_one(phone)

    return jsonify({"message": "Phone added successfully"})

if __name__ == "__main__":
    app.run()
