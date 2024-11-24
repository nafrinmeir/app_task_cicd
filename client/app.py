from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_URL = "http://server-service:5001/tasks"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add', methods=["POST"])
def add_task():
    data = {
        "title": request.form["title"],
        "description": request.form["description"],
        "priority": request.form["priority"],
        "due_date": request.form["due_date"]
    }
    response = requests.post(API_URL, json=data)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
