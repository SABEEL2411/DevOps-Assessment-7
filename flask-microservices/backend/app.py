from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def api():
    return jsonify({"message": "Hello from Flask Backend!"})

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

