import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pickle

connection = pg.connect( "host=bootcampml.postgres.database.azure.com port=5432 dbname=postgres user=bootcamp@bootcampml password=P@ssword123 sslmode=require")
#dataframeWF = psql.read_sql("SELECT * from breast_cancer", connection)
dataframe = psql.read_sql("SELECT CASE WHEN age <= 69 THEN '60-69' WHEN (age >= 70 AND age <= 79)  THEN '70-79' WHEN (age >= 80 AND age <= 89) THEN '80-89' WHEN age >= 90  THEN '90+' ELSE ' '  END AS age_range, COUNT(*) AS count_range FROM breast_cancer WHERE cancer_diagnosis = true GROUP BY CASE WHEN age <= 69 THEN '60-69' WHEN (age >= 70 AND age <= 79)  THEN '70-79' WHEN (age >= 80 AND age <= 89) THEN '80-89'  WHEN age >= 90  THEN '90+' ELSE ' '  END;", connection)


app = Flask(__name__)
db = SQLAlchemy()
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://bootcamp@bootcampml:P@ssword123@bootcampml.postgres.database.azure.com:5432/postgres"
db.init_app(app)

class BreastCancer(db.Model):
    __tablename__ = "breast_cancer"
    patients_birads = db.Column(db.String(50), primary_key = True)
    hormone_therapy = db.Column(db.String(10))
    family_history = db.Column(db.String(10))
    comparison_mammogram = db.Column(db.String(10))
    breast_biopsy = db.Column(db.String(10))
    cancer_diagnosis = db.Column(db.Boolean)
    age = db.Column(db.Integer)

@app.route("/")
def index():
    return render_template("breast_cancer.html")

@app.route("/age_range")
def welcome():
    """List all available api routes."""
    return (
        dataframe.to_json(orient="table")
    )

@app.route("/data/<age>/<birads>/<biopsy>/<mammogram>/<family>/<hormone>")
def data(age,birads,biopsy,mammogram,family,hormone):
    loaded_model = pickle.load(open("model.sav", 'rb'))
    predictors = [age,birads,biopsy,mammogram,family,hormone]
    result = loaded_model.predict([predictors])
    cancer = False
    if result[0] == 1:
        cancer=True
    return str(cancer)

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
