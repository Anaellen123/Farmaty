#administrar 80mg/ kg por dia a cada 6horas


class calculo:
    def __init__(self, dosagem, mg, ml,hora):
        self.dosagem = dosagem
        self.mg = mg
        self.ml = ml
        self.hora = hora

    def total_consumo(self, dosagem):
        mg_total = dosagem
        mg
def app ():
    div_horario = horas_dia()

def consumo_ml():

    print("quantas mg{}/ml{}(miligrama por ml) vem no frasco?")
    mg = int(input(" quantos mg? :"))
    ml = int(input("quantas ml? :"))
    quantidade_mg_dose = int(input("quantas miligramas por dose? :"))
    dose_ml = 1
    calc1 = mg * dose_ml
    calc2 = quantidade_mg_dose * ml
    result = calc2 / calc1
    print("o paciente devera tomar {}ml a cada hora preescrita".format(result))

def total_consumo():
    mg_total =int(input("qual dosagem diaria a ser consumida? :"))
    vezes_a_tomar = int(input("preescrição de quantas vezes ao dia? :"))
    total_por_dose = mg_total / vezes_a_tomar
    print(total_por_dose)
def dosagem_kilo():
    dosagem = int(input("Qual a dosagem :"))
    kilos = int(input("quantos kilos :"))
    multiplicacao = dosagem * kilos
    print(multiplicacao)

def horas_dia():
    vezes = int(input("Irá tomar quantas vezes ao dia? :"))
    divs = 24 / vezes
    print("Ira tomar o medicamento a cada {} horas".format(divs))
if __name__ == ("__main__") :
    app()