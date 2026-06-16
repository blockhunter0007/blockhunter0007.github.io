from flask import Flask, send_from_directory
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route('/<path:path>')
def serve(path):
    if os.path.isfile(os.path.join(script_dir, path)):
        return send_from_directory(script_dir, path)
    elif os.path.isdir(os.path.join(script_dir, path)):
        return send_from_directory(script_dir, path + '/index.html')
    else:
        return "File not found", 404

@app.route('/')
def index():
    return send_from_directory(script_dir, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)