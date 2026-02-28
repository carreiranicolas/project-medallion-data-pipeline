# Salvando o caminho dos arquivos em uma lista

from pathlib import Path


ABS_PATH = Path('.').resolve()


BRONZE_PATH = ABS_PATH.joinpath('data/1_bronze')

print(f'Salvando o caminho {BRONZE_PATH} para a leitura de arquivos')
print()

ARQUIVOS = [arquivo for arquivo in BRONZE_PATH.iterdir()]

print('Leitura de arquivos realizada')
print()


# print('Ordem dos arquivos na lista de arquivos:')

# for i, arquivo in enumerate(ARQUIVOS):
#     print(f'{i} - {arquivo}')



