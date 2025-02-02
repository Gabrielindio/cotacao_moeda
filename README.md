# Dashboard Interativo de Cotações de Moedas no Power BI

## Descrição do Projeto
Este projeto visa a coleta de cotações diárias de diversas moedas em relação ao real (BRL) por meio da API "AwesomeAPI" e a criação de um dashboard interativo no Power BI para visualização dos dados.

## Funcionalidades
- Coleta automática de dados de cotação de até 19 moedas.
- Conversão de timestamps para datas legíveis.
- Formatação dos valores para padrão brasileiro.
- Extração de informações temporais (Ano, Mês, Nome do Mês e Dia).
- Exportação dos dados para o Power BI para análise e visualização interativa.

## Tecnologias Utilizadas
- **Linguagem:** Python 3
- **Bibliotecas:**
  - `requests` para requisição de dados via API
  - `pandas` para manipulação de dados
  - `datetime` para manipulação de datas
  - `locale` para formatação de datas no padrão PT-BR
  - `matplotlib` (embora não usada diretamente no código atual, pode ser útil para visualização local)
- **API Utilizada:** AwesomeAPI (https://docs.awesomeapi.com.br/)
- **Ferramenta de Visualização:** Power BI

## Estrutura do Código
1. **Definição das moedas para análise**
2. **Configuração do período de coleta**
3. **Requisição de dados para cada moeda**
4. **Processamento e formatação dos dados**
5. **Criação do DataFrame final para análise**
6. **Exportação para uso no Power BI**

## Como Executar o Projeto
1. **Instalar as dependências:**
   ```sh
   pip install requests pandas matplotlib
   ```
2. **Executar o script Python:**
   ```sh
   python coletar_cotacoes.py
   ```
3. **Exportar o DataFrame para CSV ou Excel para carregamento no Power BI:**
   ```python
   df.to_csv('cotacoes_moedas.csv', index=False, encoding='utf-8')
   ```
4. **Carregar os dados no Power BI e construir os dashboards.**

## Melhorias Futuras
- Automatização da coleta de dados diária.
- Implementação de armazenamento em banco de dados.
- Integração direta do Python com o Power BI via API.

