from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Flask API!"})

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    time.sleep(0.1)  # Simulate processing delay
    return jsonify({"received": data})

@app.route("/error")
def error():
    return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(debug=True)
