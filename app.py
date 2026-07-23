import pandas as pd
from flask import Flask, render_template, request
import pickle


df = pd.read_csv("company_esg_financial_dataset.csv")

app = Flask(__name__)


model = pickle.load(open("model.pkl", "rb"))




@app.route('/')
def home():
    return render_template("index.html")




@app.route('/predict')
def predict():
    return render_template("predict.html")



@app.route('/about')
def about():
    return render_template("about.html")




@app.route('/dashboard')
def dashboard():

    total = len(df)
    avg = round(df["ESG_Overall"].mean(), 2)
    highest = round(df["ESG_Overall"].max(), 2)
    lowest = round(df["ESG_Overall"].min(), 2)

    return render_template(
        "dashboard.html",
        total=total,
        avg=avg,
        highest=highest,
        lowest=lowest
    )



@app.route('/result', methods=['POST'])
def result():

    e = float(request.form['environment'])
    s = float(request.form['social'])
    g = float(request.form['governance'])

    prediction = round(model.predict([[e, s, g]])[0], 2)


    if prediction >= 80:
        rating = "Excellent 🟢"
        message = "This company demonstrates excellent sustainability performance."

    elif prediction >= 60:
        rating = "Good 🔵"
        message = "This company has good ESG performance with room for improvement."

    elif prediction >= 40:
        rating = "Average 🟡"
        message = "This company has an average sustainability performance."

    else:
        rating = "Poor 🔴"
        message = "This company needs significant improvement in ESG practices."

    return render_template(
        "predict.html",
        prediction=prediction,
        environment=e,
        social=s,
        governance=g,
        rating=rating,
        message=message
    )



if __name__ == "__main__":
    app.run(debug=True)