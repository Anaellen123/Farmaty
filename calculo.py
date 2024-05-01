#administrar 80mg/ kg por dia a cada 6horas

def app ():
    #dosagem_por_kilo = dosagem_kilo()
    #dosagem_por_hora = total_consumo()
    dosagem_por_ml_a_hora = consumo_ml()

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


if __name__ == ("__main__") :
    app()