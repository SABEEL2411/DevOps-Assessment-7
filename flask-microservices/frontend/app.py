from flask import Flask, render_template_string
import requests

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Frontend</title>
</head>
<body>
    <h1>Frontend - Flask</h1>
    <p>Message from Backend:</p>
    <pre>{{ message }}</pre>
</body>
</html>
"""

@app.route('/')
def index():
    try:
        res = requests.get("http://backend-service:5000/api", timeout=2)
        message = res.json().get("message")
    except Exception as e:
        message = f"Error connecting to backend: {e}"
    return render_template_string(HTML, message=message)

@app.route('/health')
def health():
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

