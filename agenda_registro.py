from datetime import datetime, timedelta

#data
hoje = datetime.now()
print(hoje.date())
print(hoje.hour)

#a função timedelta serve para realizar contas com dastas


#variações de datas
amanha = hoje + timedelta(days=1)
print(amanha)

data_contrato = datetime(year=2022, month=9, day=1)
atraso = hoje - data_contrato
print(atraso.days)

#observação datas mais recentes são maiores que as datas mais atigas

#extrair datas em outros formatos
data_contrato = "01/06/2024"
data_contrato = datetime.strptime(data_contrato, "%d/%m/%Y")
print(data_contrato)

#formato brasileiro
hoje.strftime("%d/%m/%Y")

#fuso horario
hoje = hoje - timedelta(hours=1)
print(hoje)


#biblioteca para fuso horarios tem que fazer intalação "pip install tzdata"

import zoneinfo
print(zoneinfo.available_timezones())
zona = zoneinfo.ZoneInfo('Singapore')
agora_singapore = hoje.astimezone(zona)
print(agora_singapore)


