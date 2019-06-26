# O objetivo desse script é copiar todos os arquivos de uma mesma empresa e
# cola-los na pasta dessa empresa.

print('Comecei')

import shutil, os

# lista de empresas e cnpj's
empresas_lista = [
    ('00000000000000', 'Z:\\\\PASTA\\\\DO\\\\CLIENTE 1'),
    ('14385673000111', 'Z:\\\\PASTA\\\\DO\\\\CLIENTE 2')
]

empresas = dict(empresas_lista)

pasta = 'C:\\\\PASTA\\\\ONDE\\\\ESTAO\\\\OS\\\\ARQUIVOS'
os.chdir(pasta)
arquivos = os.listdir(pasta) #CRIA UMA LISTA COM CADA ARQUIVO DE PASTA
for arq in arquivos :
    for cnpj in empresas :
        if cnpj in arq :
            nomeCompleto = pasta + '\\\\' + arq
            print(f'Achei!!\nArquivo: {arq}\nCaminho do arquivo: {nomeCompleto}\nDestino do arquivo: {empresas[cnpj]}')
            shutil.copy(nomeCompleto, empresas[cnpj])
            break
print('Acabei')
