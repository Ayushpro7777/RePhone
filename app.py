from flask import Flask
from database import init_db
from routes import api
import os

app = Flask(__name__)

init_db()
app.register_blueprint(api)

@app.route("/")
def home():
    return "RePhone backend running successfully"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
