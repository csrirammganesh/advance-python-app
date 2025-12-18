import os
from flask import Flask

app = Flask(__name__)

# Read ENV variables
port = int(os.environ.get("PORT", 5000))
env = os.environ.get("FLASK_ENV", "development")

@app.route("/")
def hello():
    return f"Hello! Running in {env} mode on port {port}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
