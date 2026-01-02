from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Sample phone data (SINGLE SOURCE OF TRUTH)
phones = [
    {
        "id": 1,
        "name": "iPhone 14",
        "price": "₹70,000",
        "image": "iphone.jpg"
    },
    {
        "id": 2,
        "name": "Samsung S23",
        "price": "₹65,000",
        "image": "samsung.jpg"
    }
]

@app.route("/")
def home():
    return "RePhone Backend Running"

@app.route("/phones")
def phone_list():
    return render_template("phones.html", phones=phones)

@app.route("/api/phones")
def api_phones():
    return jsonify(phones)

@app.route("/upload", methods=["POST"])
def upload_image():
    if 'image' not in request.files:
        return "No image found", 400

    image = request.files['image']
    if image.filename == "":
        return "No selected file", 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(filepath)

    return "Image uploaded successfully"

if __name__ == "__main__":
    app.run(debug=True)
