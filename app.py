from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/unpickle', methods=['POST'])
def safe_method():
    data = request.json  # Use JSON data
    return jsonify(data)  # Return JSON response

if __name__ == "__main__":
    app.run(debug=True)
