#administrar 80mg/ kg por dia a cada 6horas

def app ():
    dosagem = int(input("Qual a dosagem :"))
    kilos = int(input("quantos kilos :"))
    conta= dosagem_kilo(dosagem, kilos)
    return conta

def dosagem_kilo(x, y):

    multiplicacao = x * y
    print(multiplicacao)


if __name__ == ("__main__") :
    app()