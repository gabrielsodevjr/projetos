import pandas as pd
import os

# Pega o caminho da pasta raiz do projeto (onde o script está)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Define os caminhos para os arquivos bronze (raw) e silver (limpo)
bronze_path = os.path.join(BASE_DIR, 'data', 'bronze', '2004-2021.tsv')
silver_path = os.path.join(BASE_DIR, 'data', 'silver', '2004-2021_limpo.csv')

def carregar_dados():
    """
    Lê o arquivo bruto .tsv da camada bronze e retorna um DataFrame pandas.
    """
    df = pd.read_csv(bronze_path, sep='\t')  # lê o arquivo com separador tab
    return df

def substituir_valores_invalidos(df):
    """
    Substitui os valores placeholders '-99999.0' (string) e -99999.0 (float)
    por pd.NA para facilitar o tratamento de dados faltantes.
    """
    df = df.replace('-99999.0', pd.NA)  # substitui string '-99999.0' por NaN
    df = df.replace(-99999.0, pd.NA)    # substitui float -99999.0 por NaN
    return df

def converter_tipos(df):
    """
    Converte as colunas de datas para datetime e colunas numéricas de texto para float.
    """
    # Converte as datas (pode colocar errors='coerce' para forçar erros virarem NaT)
    df['DATA INICIAL'] = pd.to_datetime(df['DATA INICIAL'], errors='coerce')
    df['DATA FINAL'] = pd.to_datetime(df['DATA FINAL'], errors='coerce')

    # Lista das colunas numéricas que estão como texto e precisam virar float
    colunas_numericas = [
        'MARGEM MÉDIA REVENDA',
        'PREÇO MÉDIO DISTRIBUIÇÃO',
        'DESVIO PADRÃO DISTRIBUIÇÃO',
        'PREÇO MÍNIMO DISTRIBUIÇÃO',
        'PREÇO MÁXIMO DISTRIBUIÇÃO',
        'COEF DE VARIAÇÃO DISTRIBUIÇÃO'
    ]

    # Converte cada coluna para numérico, forçando erro a virar NaN
    for coluna in colunas_numericas:
        df[coluna] = pd.to_numeric(df[coluna], errors='coerce')

    return df

def verificar_qualidade_dados(df):
    """
    Exibe métricas de qualidade dos dados para você analisar:
    - Quantidade de linhas duplicadas
    - Quantidade de valores nulos por coluna
    - Quantidade de valores <= 0 nas colunas de preço (sinal de erro)
    """
    print(f'Duplicados encontrados: {df.duplicated().sum()}')

    print('Valores nulos por coluna:')
    print(df.isnull().sum())

    colunas_preco = [
        'PREÇO MÉDIO REVENDA',
        'PREÇO MÍNIMO REVENDA',
        'PREÇO MÁXIMO REVENDA',
        'PREÇO MÉDIO DISTRIBUIÇÃO',
        'PREÇO MÍNIMO DISTRIBUIÇÃO',
        'PREÇO MÁXIMO DISTRIBUIÇÃO'
    ]

    for col in colunas_preco:
        count = (df[col] <= 0).sum()
        print(f'Valores <= 0 na coluna {col}: {count}')

def limpar_dados():
    """
    Função principal que executa a limpeza dos dados:
    - Carrega os dados brutos
    - Substitui valores inválidos por NaN
    - Converte tipos das colunas
    - Remove linhas com valores nulos
    - Verifica qualidade dos dados
    - Salva o dataframe limpo na camada silver
    """
    df = carregar_dados()
    df = substituir_valores_invalidos(df)
    df = converter_tipos(df)

    verificar_qualidade_dados(df)

    df.to_csv(silver_path, index=False)
    print(f'Dados limpos e salvos em {silver_path}')

if __name__ == "__main__":
    limpar_dados()
