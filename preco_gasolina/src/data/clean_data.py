import pandas as pd
import os

# Pega o caminho da pasta raiz do projeto (onde o script está)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Define os caminhos para os arquivos bronze e silver
bronze_path = os.path.join(BASE_DIR, 'data', 'bronze', '2004-2021.tsv')
silver_path = os.path.join(BASE_DIR, 'data', 'silver', '2004-2021_limpo.csv')

def limpar_dados():
    # 1. Ler o arquivo tsv do bronze_path
    df = pd.read_csv(bronze_path, sep='\t')
    # 2. Remover linhas com valores nulos
    df_limpona = df.dropna()
    # 3. Salvar o dataframe limpo em silver_path
    df_limpona.to_csv(silver_path, index=False)
    # 4. Imprimir mensagem de sucesso
    print(f'Dados limpos e salvos em {silver_path}')
  
# Executa a função de limpeza de dados se o script for executado diretamente   
if __name__ == "__main__":
    limpar_dados()