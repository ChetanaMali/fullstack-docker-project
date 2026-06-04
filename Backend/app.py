from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json
import traceback

load_dotenv()

app = Flask(__name__)
CORS(app)

client = MongoClient(os.getenv("MONGO_URI"))
db = client["studentdb"]
collection = db["users"]

@app.route('/api')
def api():

    with open('data.json') as f:
        data = json.load(f)

    return jsonify(data)



@app.route('/submit', methods=['POST'])
def submit():

    try:

        print("Received Data:")
        print(request.json)

        data = request.json

        collection.insert_one(data)

        return jsonify({
            "message": "success"
        })

    except Exception as e:

        print("\n========== ERROR ==========")
        traceback.print_exc()
        print("===========================\n")

        return jsonify({
            "error": str(e)
        }), 500
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)