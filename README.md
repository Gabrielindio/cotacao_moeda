Este código realiza a coleta de cotações diárias de várias moedas (USD, EUR, GBP, etc.) contra o Real Brasileiro (BRL) utilizando a API AwesomeAPI e processa esses dados com a biblioteca pandas para análise. O fluxo do código pode ser resumido da seguinte forma:

Definição das Moedas para Análise: Uma lista de pares de moedas é definida, como USD-BRL, EUR-BRL, entre outras.
Definição do Período de Coleta: O código define um intervalo de datas para coletar as cotações, começando em 1º de janeiro de 2022 até o dia anterior à data atual.
Coleta de Dados: Utilizando a biblioteca requests, é feita uma requisição para a API para obter as cotações diárias de cada moeda. O retorno é um JSON com dados como o valor de fechamento, alta, baixa e o timestamp da data.
Tratamento dos Dados:
Conversão de Dados: Os valores de fechamento, alta e baixa são convertidos para o formato numérico com duas casas decimais.
Extração de Componentes da Data: O código extrai o ano, o nome do mês (em português), o número do mês e o dia da data para cada cotação.
Conversão para DataFrame: Os dados são organizados em um DataFrame do pandas, sendo removidos duplicados por "Data" e "Moeda".
Integração com Power BI: O DataFrame gerado pode ser exportado para análise no Power BI. Para isso, você pode gerar relatórios e dashboards visualizando as variações de fechamento de moedas ao longo do tempo. O Power BI pode utilizar as colunas como "Ano", "Mês", "Data", "Fechamento", "Alta" e "Baixa" para criar gráficos e cálculos, como o crescimento ou queda das moedas em períodos mensais.
O tratamento de dados no Python inclui a formatação de números, a transformação de timestamps em datas legíveis e a extração de partes específicas dessas datas para análise mais detalhada, facilitando a visualização e comparação de cotações no Power BI.
