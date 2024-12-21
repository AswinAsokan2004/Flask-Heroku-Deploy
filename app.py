from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post_method():
    data = request.get_json()  # Extract JSON data from the request
    if data and "1" in data:
        return jsonify(message=f"hello {data['1']}")
    else:
        return jsonify(error="Key '1' not found in request data"), 400

if __name__ == '__main__':
    app.run(debug=True)
