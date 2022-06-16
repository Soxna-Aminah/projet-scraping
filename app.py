from flask import Flask, jsonify, render_template
from flask_cors import CORS
from controller import *
from model.modele import *

app=Flask(__name__)
CORS(app)


@app.route("/")
def home():
    data=recupmeubles()
    return render_template('home.html',data=data)


@app.route("/donnes")
def donnees():
    data=recupmeubles()
   
    return(jsonify(data))




if __name__=='__main__':

    app.run(debug=True)
