from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://mongodb:27017/")
db = client["taskdb"]
tasks_collection = db["tasks"]

@app.route('/tasks', methods=["POST"])
def add_task():
    task = request.json
    tasks_collection.insert_one(task)
    return jsonify({"message": "Task added successfully"}), 201

@app.route('/tasks', methods=["GET"])
def get_tasks():
    tasks = list(tasks_collection.find({}, {"_id": 0}))
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
