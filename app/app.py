# Trigger DEV workflow
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Hello from DevOps App 🚀",
        "environment": os.getenv("ENV_NAME"),
        "debug": os.getenv("DEBUG"),
        "log_level": os.getenv("LOG_LEVEL"),
        "database": os.getenv("DB_URL")
    }

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        debug=os.getenv("DEBUG") == "true"
    )
