from flask import Flask, jsonify, render_template, request
import os

app = Flask(__name__)

phones = [
    {
        "id": 1,
        "name": "iPhone 13",
        "price": "₹55,000",
        "image": "https://via.placeholder.com/150"
    },
    {
        "id": 2,
        "name": "Samsung S21",
        "price": "₹40,000",
        "image": "https://via.placeholder.com/150"
    }
]

@app.route("/")
def home():
    return "RePhone backend running successfully"

@app.route("/api/phones")
def get_phones():
    return jsonify(phones)

@app.route("/phones")
def phones_page():
    return jsonify(phones)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

