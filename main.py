from flask import Flask, jsonify
from flask_cors import CORS

import datetime

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_info():
    response = {
        "email": "andrewduran12355@gmail.com",
        "current_datetime": datetime.datetime.utcnow().isoformat() + 'Z',
        "github_url": "https://github.com/CloudPro2/public-api-hngtask0"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
