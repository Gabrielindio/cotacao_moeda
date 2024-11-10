import requests as rq
import pandas as pd
import matplotlib
from datetime import datetime as dt, timedelta as td
import locale

# ======================================================= DEFINIR AS MOEDAS PARA ANALISE ===========================================
moedas = ['USD-BRL','EUR-BRL', 'CHF-BRL', 'AUD-BRL', 'CAD-BRL', 'NZD-BRL', 'GBP-BRL', 'SGD-BRL', 'HKD-BRL', 'ZAR-BRL', 'JPY-BRL', 'CNY-BRL', 'INR-BRL', 'MXN-BRL', 'SAR-BRL', 'AED-BRL', 'ILS-BRL', 'PLN-BRL', 'TRY-BRL']
start_date = '20220101'
end_date = (dt.now() - td(days=1)).strftime('%Y%m%d') #RETORNA A DATA ATUAL -1 NO FORMATO 'ANOMESDIA'
periodo = (dt.now() - td(days=1) - dt.strptime('2022-01-01', '%Y-%m-%d')).days # RETORNA QTD DE DIAS ATÉ A DATA ATUAL -1
dados_moedas = []

# ======================================================= REALIZAR A REQUISIÇÃO DAS MOEDAS===========================================
for moeda in moedas:
    url = f'https://economia.awesomeapi.com.br/json/daily/{moeda}/{periodo}/?start_date={start_date}&end_date={end_date}'
    response = rq.get(url)
    
    if response.status_code == 200:
        dados_json = response.json()
        
        # REALIZAR A COLETA DOS DADOS POR DIA 
        for dia in dados_json:
            dados_moedas.append({
                "Moeda": moeda,  # TRAZER DIRETAMENTE A MOEDA (ex. 'USD-BRL')
                "Fechamento": dia.get('bid'),
                "Alta": dia.get('high'),
                "Baixa": dia.get('low'),
                "Data": dt.fromtimestamp(int(dia.get('timestamp'))).strftime('%Y-%m-%d')  # CONVERTAR O TIMESTAMP PARA DATA
            })
    else:
        print(f'Erro ao acessar a API para {moeda}: {response.status_code}')

df = pd.DataFrame(dados_moedas).drop_duplicates(subset=["Data", "Moeda"], keep='first')

for coluna in ['Fechamento', 'Alta', 'Baixa']: #MUDAR O TIPO DE DADO PARA DECIMAL
    df[coluna] = df[coluna].astype(float).map("{:,.2f}".format).str.replace('.', ',')


#EXTRAIR O ANO DA COLUNA DATA
df['Ano'] = pd.to_datetime(df['Data']).dt.year

#EXTRAIR O MES DA COLUNA DATA
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8') 
df['Nomes_mes'] = pd.to_datetime(df['Data']).dt.strftime('%b')

#EXTRAIR O MES EM FORMATO DE NUMERO
df['Mes'] = pd.to_datetime(df['Data']).dt.month

#EXTRAIR O DIA DA COLUNA DATA
df['Dia'] = pd.to_datetime(df['Data']).dt.day

# Exibe os dados coletados como uma lista de dicionários
print(df)
