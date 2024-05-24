from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)


class dosagem:
     def __init__(self, dose, mg, ml):
          self.dose = dose
          self.mg = mg
          self.ml = ml


lista = []

@app.route("/")
def index():

     return render_template("index.html", titulo='Posologia', paciente=lista)

@app.route('/criar', methods=['POST', ])
def criar():
     dose = request.form['dose']
     mg = request.form['mg']
     ml = request.form['ml']
     poso = dosagem(dose, mg, ml)
     lista.append(poso)
     return render_template('index.html', paciente=lista)



app.run(debug=True)