#import psycopg2 as pg
#import pandas.io.sql as psql
import pandas as pd
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

#connection = pg.connect( "host=bootcampml.postgres.database.azure.com port=5432 dbname=postgres user=bootcamp@bootcampml password=P@ssword123 sslmode=require")
#dataframeWF = psql.read_sql("SELECT * from breast_cancer", connection)


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

@app.route("/data/<age>/<birads>/<HT>/<FH>/<MG>/<BB>")
def data(age,birads,HT,FH,MG,BB):

    #request.json
    # results = BreastCancer.query\
    #     .with_entities(BreastCancer.patients_birads,BreastCancer.hormone_therapy,BreastCancer.family_history,BreastCancer.comparison_mammogram,BreastCancer.breast_biopsy,BreastCancer.cancer_diagnosis,BreastCancer.age)\
    #     .filter(BreastCancer.patients_birads==birads)\
    #     .filter(BreastCancer.hormone_therapy==HT)\
    #     .filter(BreastCancer.family_history==FH)\
    #     .filter(BreastCancer.comparison_mammogram==MG)\
    #     .filter(BreastCancer.breast_biopsy==BB)\
    #     .filter(BreastCancer.age==age)\
    #     .all()
    # results = pd.DataFrame(results)
    # return (results.to_json(orient="records"))
    return "hola"


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
