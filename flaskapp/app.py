import os
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.post("/echo")
def echo():
    data = request.get_json(force=True)
    return jsonify(received=data), 200


if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 5001))
    app.run(debug=True, port=PORT)
