from flask import Flask, jsonify, request
import socket

app = Flask(__name__)
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Flask API!"})

@app.route('/ping')
def ping():
    server_host = request.host 
    ip_address = socket.gethostbyname(socket.gethostname())
    return jsonify({"message": "pong",
                    "serverAddress": server_host,
                    "actualServerAddress": ip_address})

@app.route('/api/hello/<name>')
def hello(name):
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/api/status')
def status():
    return jsonify({"status": "API is running"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)