from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)




@app.route("/")
def index():
     return render_template("index.html")


@app.route('/index', methods=['POST',])
def consumo_ml():

    quantidade_mg_dose = request.form['dose']
    mg = request.form['mg']
    ml = request.form['ml']
    dose_ml = 1
    calc1 = mg * dose_ml
    calc2 = quantidade_mg_dose * ml
    result = calc2 / calc1
    result.append[result]

    return  redirect(url_for('index'))


app.run(debug=True)