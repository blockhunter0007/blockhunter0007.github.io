from flask import Flask, send_from_directory
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
@app.route('/<path:path>')
def serve(path):
    out_put_file = ""
    if os.path.isfile(os.path.join(script_dir, path)):
        out_put_file = path
    elif os.path.isdir(os.path.join(script_dir, path)):
        out_put_file = path + "/index.html"
    elif os.path.exists(path):
        out_put_file = path
    else:
        #print(f"{script_dir}  {path}")
        return "error"
    with open(out_put_file, "rb") as file:
        output = file.read()
        try:
            output = output.decode("utf-8")
            #print(output)
            return output.replace("https://blockhunter0007.github.io/", "http://127.0.0.1:5000/")
        except:
            return output

@app.route('/')
def index():
    return send_from_directory(script_dir, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)