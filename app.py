from flask import Flask, request,jsonify, render_template
import pickle
import joblib
from joblib import load
import pandas as pd
Flask_app = Flask(__name__)
model = pickle.load(open('best_decision_tree_model.pkl','rb'))




# Load your machine learning model




@Flask_app.route("/")
def index():
    return render_template("index.html")

@Flask_app.route("/result", methods=['POST'])
def result():
    SIZE = request.form['SIZE']
    FUEL = request.form['FUEL']
    DISTANCE = request.form['DISTANCE']
    DECIBLE = request.form['DECIBLE']
    AIRFLOW = request.form['AIRFLOW']
    FREQUENCY = request.form['FREQUENCY']

    # Use the loaded model to make predictions based on the form inputs
    # For example, assuming the model.predict method is available in your model:
    # result = model.predict([[size, fuel, distance, decibel, airflow, frequency]])

    # Replace the static result message with the actual prediction
    result = "The fire is in the extension state"


    return render_template('index.html',result=result)

if __name__ == "__main__" :
    Flask_app.run(debug=True)
