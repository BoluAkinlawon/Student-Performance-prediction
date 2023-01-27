import flask
from flask import Flask, request, jsonify
import pickle
import json
import numpy as np

app = Flask(__name__)
model = pickle.load(open('ann_model.pkl', 'rb'))

@app.route('/')
def home():
    return 'Welcome to Student Performance Prediction'

@app.route("/predict", methods = ["GET"])
def predict():
    gender = request.args.get("gender")
    place_of_residence = request.args.get("hypertension")
    parent_marital_status= request.args.get("heart_disease")
    family_size = request.args.get("ever_married")
    mode_of_transportation = request.args.get("work_type")
    elementary_education = request.args.get("Residence_type")
    higher_institution_location = request.args.get("avg_glucose_level")

    makeprediction = model.predict([[gender, place_of_residence, parent_marital_status, family_size, mode_of_transportation, elementary_education, higher_institution_location]])
    output = round(makeprediction[0],0)
    return jsonify({'Your predicted score is':output})
    
    print("Done")
if __name__ =="__main__":
    app.run(debug=True)
