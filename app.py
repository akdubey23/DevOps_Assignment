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

if __name__ == "__main__":
    app.run(debug=True)