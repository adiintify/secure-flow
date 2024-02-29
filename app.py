import pickle
from flask import Flask, request

app = Flask(__name__)

# A simple route to deserialize data received over the network

@app.route('/unpickle', methods=['POST'])
def unpickle():
    data = request.data  # WARNING: This is unsafe!
    obj = pickle.loads(data)  # Insecure deserialization
    return "Object deserialized!"


if __name__ == "__main__":
    app.run(debug=True)
