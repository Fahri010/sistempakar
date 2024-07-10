from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from fuzzy import fuzzy_logic

import pickle
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=["GET"])
def home():
    return render_template("coba.html")


@app.route('/', methods=["POST", "OPTIONS"])
@cross_origin()
def submit():
    # Dapatkan data dari JSON
    data = request.get_json()

    # change to dictionary
    data = dict(data)

    # Data Must Like This
    """
    {
        'C01': 0, 'C02': 70, 'C03': 0,
        'C04': 0, 'C05': 70, 'C06': 0,
        'C07': 30, 'C08': 0, 'C09': 0,
        'C10': 0, 'C11': 0, 'C12': 50,
        'C13': 10, 'C14': 0, 'C15': 0,
        'C16': 30, 'C17': 0, 'C18': 0,
        'C19': 0, 'C20': 70, 'C21': 0,
        'C22': 0, 'C23': 0, 'C24': 70,
        'C25': 0, 'C26': 0, 'C27': 80,
        'C28': 0, 'C29': 0, 'C30': 60
    }

    {
        'C01': 80, 'C02': 0, 'C03': 0, 
        'C04': 80, 'C05': 0, 'C06': 0, 
        'C07': 80, 'C08': 0, 'C09': 0, 
        'C10': 80, 'C11': 0, 'C12': 0, 
        'C13': 80, 'C14': 0, 'C15': 0, 
        'C16': 80, 'C17': 0, 'C18': 0, 
        'C19': 80, 'C20': 0, 'C21': 0, 
        'C22': 80, 'C23': 0, 'C24': 0, 
        'C25': 80, 'C26': 0, 'C27': 0, 
        'C28': 80, 'C29': 0, 'C30': 0
    }
    """
    # validate data
    if not data:
        return jsonify({"error": "Data tidak ditemukan"})
    
    # Get the result
    result = fuzzy_logic(    {
           'C01': 80, 'C02': 0, 'C03': 0, 
        'C04': 80, 'C05': 0, 'C06': 0, 
        'C07': 80, 'C08': 0, 'C09': 0, 
        'C10': 80, 'C11': 0, 'C12': 0, 
        'C13': 80, 'C14': 0, 'C15': 0, 
        'C16': 80, 'C17': 0, 'C18': 0, 
        'C19': 80, 'C20': 0, 'C21': 0, 
        'C22': 80, 'C23': 0, 'C24': 0, 
        'C25': 80, 'C26': 0, 'C27': 0, 
        'C28': 80, 'C29': 0, 'C30': 0
    })

    print(result)

    # return jsonify(result)
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
