from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "Mini DevOps App",
        "status": "running",
        "message": "Hello from the DevOps revision project!"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/hello")
def hello():
    return jsonify({
        "message": "DevOps revision is working!"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
