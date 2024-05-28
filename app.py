from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)


class dosagem:
     def __init__(self, dose, mg, ml, hora):
          self.dose = dose
          self.mg = mg
          self.ml = ml
          self.hora = hora

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

     def horas_dia(self, hora):
          vezes = hora
          divs = 24 / vezes
          return int(divs)


lista = []



@app.route("/")
def index():

     return render_template("index.html")

@app.route('/criar', methods=['POST', ])
def criar():
     dose = int(request.form['dose'])
     mg = int(request.form['mg'])
     ml = int(request.form['ml'])
     hora = int(request.form['hora'])
     poso = dosagem(dose, mg, ml, hora)
     lista.append(poso)
     horario = "{} horas pelo tempo preescrito".format(poso.horas_dia(hora))
     result = "Será necessário {} ml a cada ".format(poso.consumo_por_ml(dose,mg,ml))



     return render_template('index.html', paciente=lista, dose = result, hora = horario)



app.run(debug=True)