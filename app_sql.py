from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# WARNING: This route is vulnerable to SQL Injection


@app.route('/search', methods=['GET'])
def search():
    user_input = request.args.get('name')
    # Vulnerable query
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
