#O objetivo desse script é copiar todos os arquivos de uma mesma empresa e
#cola-los na pasta dessa empresa.

print('Comecei')

import shutil, os
os.chdir('C:\\Users\\Administrador\\PycharmProjects\\utilidades\\')
src = 'C:\\Users\\Administrador\\PycharmProjects\\utilidades\\arquivos\\empresa1.txt'
dst = 'C:\\Users\\Administrador\\PycharmProjects\\utilidades\\empresa1'
shutil.copy(src, dst)

print('Acabei')