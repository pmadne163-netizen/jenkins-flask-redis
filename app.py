from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome To Flask Application Running on Cloud !🚀"

# Debug route (important)
@app.route("/test")
def test():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
