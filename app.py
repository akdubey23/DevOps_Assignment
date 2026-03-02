from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to ACEest Fitness & Gym DevOps Project"

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "message": "Application is running successfully"
    })

@app.route("/version")
def version():
    return jsonify({
        "version": "1.0",
        "application": "ACEest Fitness Management System"
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)