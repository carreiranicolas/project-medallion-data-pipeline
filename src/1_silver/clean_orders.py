from base import ARQUIVOS
import pandas as pd 

#Obtendo o nome do arquivo

ARQUIVO = ARQUIVOS.pop(0)

print(f"Iremos transformar o arquivo: {ARQUIVO}")


try:
    df = pd.read_csv(ARQUIVO)

    df['shipping_limit_date'] = pd.to_datetime(df['shipping_limit_date'])


except Exception as e:
    print(f'ERRO: {e}')
    print(f'Except name: {e.__class__.__name__}')