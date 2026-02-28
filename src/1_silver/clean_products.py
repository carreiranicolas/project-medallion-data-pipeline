from base import ARQUIVOS
import pandas as pd

#Obtendo o nome do arquivo

ARQUIVO = ARQUIVOS.pop(3)

print(f"Iremos transformar o arquivo: {ARQUIVO}")
print()


try:
    df = pd.read_csv(ARQUIVO)


    print(df['product_photos_qty'])


except Exception as e:
    print(f'ERRO: {e}')
    print(f'Except name: {e.__class__.__name__}')