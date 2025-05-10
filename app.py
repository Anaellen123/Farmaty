from flask import Flask, render_template, request, redirect, url_for, session
import markdown2

#from: está chamando o módulo “flask”

#import: está importando a classe “Flask” de dentro do módulo “flask”

#render_template: Função que permite renderizar arquivos HTML armazenados na pasta, templates facilitando a separação entre lógica de programação e interface.

#request: Objeto que lida com requisições HTTP(como GET e POST), permitindo o recebimento de dados enviados por formulários

#redirect: Função usada para redirecionar o usuário para outra rota.

#url_for : Função que gera URLs dinâmicas baseadas no nome da rota, garantindo flexibilidade na criação de links e redirecionamentos.

#É essencial para inicializar o Flask, ajuda na configuração e organização da aplicação
app = Flask(__name__)

#classe para criação do objeto calculadora de posologia
class dosagem:

     # método construtor onde teremos os parâmetros necessários para o calculo
     def __init__(self, dose, mg, ml, hora):
          self.dose = dose
          self.mg = mg
          self.ml = ml
          self.hora = hora


     # Cálculo do medicamento
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

     # calculo de horário
     def horas_dia(self, hora):
          vezes = hora
          divs = 24 / vezes
          return int(divs)


lista = []
app.secret_key = 'sua_chave_secreta_segura'



@app.route("/")
def index():

     return render_template("index_2.html")

@app.route('/criar', methods=['POST'])
def criar():
    dose = int(request.form['dose'])
    mg = int(request.form['mg'])
    ml = int(request.form['ml'])
    hora = int(request.form['hora'])

    poso = dosagem(dose, mg, ml, hora)
    lista.append(poso)


    # Salva dados na sessão
    session['dose'] = "Será necessário {} ml a cada ".format(poso.consumo_por_ml(dose, mg, ml))
    session['hora'] = "{} horas pelo tempo preescrito".format(poso.horas_dia(hora))
    session['posologia'] = "Para tomar {}mg da dose prescrita".format(poso.dose)


    return redirect(url_for('resultado'))

@app.route('/resultado', methods=['GET'])
def resultado():
    dose = session.get('dose')
    hora = session.get('hora')
    posologia = session.get('posologia')

    return render_template('index_2.html', posologia=posologia,dose=dose, hora=hora)

@app.route("/medicamentos")
def medicamentos ():
     medicamentos_lista = "medicamentos_lista.html"
     return render_template(medicamentos_lista)

@app.route("/conhecimento")
def conhecimento():
    return redirect(url_for('mostrar_conhecimento'))

@app.route("/mostrar_conhecimento")
def mostrar_conhecimento():
    conteudo_html = ler_conteudo_markdown("markdown/conhecimentopr1.md")
    return render_template("conhecimento.html", texto=conteudo_html)


def ler_conteudo_markdown(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        texto_md = f.read()
    html_convertido = markdown2.markdown(texto_md)
    return html_convertido



#app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)






