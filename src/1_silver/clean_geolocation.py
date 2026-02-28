from base import ARQUIVOS
import pandas as pd


#Obtendo o nome do arquivo

ARQUIVO = ARQUIVOS.pop(1)

print(f"Iremos transformar o arquivo: {ARQUIVO}")
print()


try:
    df = pd.read_csv(ARQUIVO)

    mapeando_estados = {
    'AC': 'Acre', 'AL': 'Alagoas', 'AP': 'Amapá', 'AM': 'Amazonas',
    'BA': 'Bahia', 'CE': 'Ceará', 'DF': 'Distrito Federal', 'ES': 'Espírito Santo',
    'GO': 'Goiás', 'MA': 'Maranhão', 'MT': 'Mato Grosso', 'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais', 'PA': 'Pará', 'PB': 'Paraíba', 'PR': 'Paraná',
    'PE': 'Pernambuco', 'PI': 'Piauí', 'RJ': 'Rio de Janeiro', 'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul', 'RO': 'Rondônia', 'RR': 'Roraima', 'SC': 'Santa Catarina',
    'SP': 'São Paulo', 'SE': 'Sergipe', 'TO': 'Tocantins'
    }
    

    df['customer_state'] = df['customer_state'].map(mapeando_estados)

    print(df['customer_city'].value_counts())


except Exception as e:
    print(f'ERRO: {e}')
    print(f'Except name: {e.__class__.__name__}')