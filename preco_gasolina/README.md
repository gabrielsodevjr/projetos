# Projeto de Análise de Preço da Gasolina no Brasil

Este projeto tem como objetivo realizar a análise exploratória e visual dos preços da gasolina no Brasil, utilizando dados públicos no formato `.tsv`.

## Estrutura do Projeto

- `data/bronze/`: dados originais brutos (raw data)
- `data/silver/`: dados tratados e limpos (cleaned data)
- `src/`: scripts para tratamento, análise e visualização dos dados
- `notebooks/`: análises exploratórias e protótipos em Jupyter Notebooks
- `reports/`: resultados finais, gráficos e relatórios

## Funcionalidades atuais

- Leitura do arquivo `.tsv` da camada bronze usando pandas
- Limpeza inicial dos dados, incluindo:
  - Substituição de valores inválidos (-99999) por NaN
  - Conversão de colunas para tipos adequados (datas, numéricos)
- Análise inicial da qualidade dos dados (valores nulos, duplicados, valores inválidos)

## Como rodar

1. Clone este repositório  
2. Crie um ambiente virtual e instale as dependências (exemplo abaixo):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   pip install pandas
