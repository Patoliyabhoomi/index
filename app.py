# app.py
from flask import Flask

# This is the Flask application object
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello 12262044!"  # Replace with your student ID

# This allows local testing
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
