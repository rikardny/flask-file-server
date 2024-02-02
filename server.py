from flask import (Flask, send_file)
import glob
import os

app = Flask(__name__)

def find_latest_file(path):
    list_of_files = glob.glob(f'{path}/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    return(latest_file)
 
@app.route('/download')
def download():
    path = find_latest_file('share')
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, port=8000, host='127.0.0.1')
