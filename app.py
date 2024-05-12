from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)


@app.route("/")
def index():
     return render_template("index.html")


@app.route('/criar', methods=['POST',])
def consumo_ml():
    mg = request.form['mg']
    ml = request.form['ml']
    quantidade_mg_dose = request.form['dose']
    dose_ml = 1
    calc1 = mg * dose_ml
    calc2 = quantidade_mg_dose * ml
    result = calc2 / calc1
    return "o paciente devera tomar {}ml a cada hora preescrita".format(result), redirect(url_for('index'))


app.run(debug=True)