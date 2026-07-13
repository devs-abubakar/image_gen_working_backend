from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.post('/generate')
def generate():
    data = request.get_json(silent=True) or {}
    prompt = data.get('prompt', '').strip()

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    result = f"Received prompt: {prompt}"
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)
