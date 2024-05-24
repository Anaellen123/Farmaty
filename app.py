from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)


class dosagem:
     def __init__(self, dose, mg, ml):
          self.dose = dose
          self.mg = mg
          self.ml = ml

     def consumo_por_ml(self, dose, mg, ml):
          quantidade_mg_dose = dose
          mg_embalagem = mg
          total_ml_da_embalagem = ml

         #regra de 3
          x = 1
          calc1 = mg_embalagem * x
          calc2 = quantidade_mg_dose * total_ml_da_embalagem
          result = calc2 / calc1
          return result


lista = []

@app.route("/")
def index():

     return render_template("index.html", paciente=lista)

@app.route('/criar', methods=['POST', ])
def criar():
     dose = request.form['dose']
     mg = request.form['mg']
     ml = request.form['ml']
     poso = dosagem(dose, mg, ml)
     lista.append(poso)
     return render_template('index.html', paciente=lista)



app.run(debug=True)