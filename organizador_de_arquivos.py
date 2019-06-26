#O objetivo desse script é copiar todos os arquivos de uma mesma empresa e
#cola-los na pasta dessa empresa.

print('Comecei')

import shutil, os

empresas_lista = [
    ('carla terezinha', ['17029944000194', 'Z:\\\\CARLA TEREZINHA2015\\\\ANO 2019\\\\JUNHO']),
    ('revista e cia', '98765432100')
]

empresas = dict(empresas_lista)

pasta = 'C:\\\\Users\\\\Administrador\\\\Documents\\\\Documentos de clientes\\\\FOLHA DE PAGAMENTO 062019\\\\SEFIP\\\\SEM FUNCIONARIOS'
print(pasta)
os.chdir(pasta)
#src = 'C:\\Users\\Administrador\\PycharmProjects\\utilidades\\arquivos\\empresa1.txt'
#dst = 'C:\\Users\\Administrador\\PycharmProjects\\utilidades\\empresa1'
#shutil.copy(src, dst)
arquivos = os.listdir(pasta)
for arq in arquivos:
    print('PRIMEIRO FOR')
    if arq[:3] == 'GPS':
        print(f'PRIMEIRO IF\n{arq[:3]}')
        for emp in empresas.values():
            print('SEGUNDO FOR')
            cnpj = emp[0]
            print(f'{cnpj}\n {arq[4:18]}')
            if arq[4:18] == cnpj:
                nomeCompleto = pasta + '\\\\' + arq
                print(f'Achei!!\n{arq}\n{nomeCompleto}\n{emp[1]}')
                break
print('Acabei')