from flask import Flask, jsonify, request
from config import HOST, PORT
import json

app = Flask(__name__)


@app.route('/reverse-sort', methods=['POST'])
def reverse_sort():

    if request.is_json:        
        try:
            request_data = json.loads(request.json)
            words = request_data['words']

            words.sort(reverse=True)
            response = jsonify({ 'words' : words })
            
            return response, 200

        except Exception as e:
            response = jsonify({ 'error' : 'Request failed' })
            return response, 400
    else:
        response = jsonify({ 'error' : 'No data provided' })
        return response, 400


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)