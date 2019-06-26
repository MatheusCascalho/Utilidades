# ORGANIZADOR DE ARQUIVOS

Contabilidades possuem diversas rotinas repetitivas e que podem tomar muito tempo de seus funcionários. Muitas dessas tarefas são automatizadas, como a geração de folha de pagamento e envio de informações da SEFIP. O próprio programa da SEFIP dá a opção de fazer o envio de informações e geração de documentos de várias empresas de uma só vez, porém o todos os arquivos são gerados em uma só pasta, ficando a cargo do funcionário colocar cada arquivo na pasta do devido cliente. Para facilitar o trabalho no escritório em que trabalho, criei um script que organizar esse documentos. 

## Funcionamento
Os arquivos gerados pelo programa da SEFIP seguem um padrão TIPODEDOCUMENTO_CNPJ. Por exemplo, uma guia da previdencia social (GPS) da empresa X cujo CNPJ é 00.000.000/0000-00 tem GPS_00000000000000 no início do nome do arquivo. Portanto, basta que o programa leia o nome do arquivo e coloque ele na pasta da empresa X. 
Mas para que ele saiba disso é necessário informar ao programa onde fica a pasta do cliente X, Y e Z. Isso é feito nessa parte do script:

```# lista de empresas e cnpj's
empresas_lista = [
    ('00000000000000', 'Z:\\\\PASTA\\\\DO\\\\CLIENTE 1'),
    ('14385673000111', 'Z:\\\\PASTA\\\\DO\\\\CLIENTE 2')
]
empresas = dict(empresas_lista)
```

Pronto! Meu script já sabe onde colocar as empresas de cada CNPJ!

Agora temos que ler o nome de cada arquivo e comparar decidir o que fazer com eles. O Python tem um modulo chamado OS que permite o acesso a documentos do sistema operacional. A função os.listdir cria uma lista com o nome de todos os arquivos da pasta que eu informar. Por comodidade, armazenei o caminho da pasta em uma variável para poder reutilizalo outras vezes no código. 

```
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
```

Essa é uma estrutura de laço aninhada. O que ela faz é comparar cada arquivo da minha pasta com os cnpj's que informei lá em cima. Se o script encontrar um cnpj cadastrado, ele copia o arquivo (por meio da função shutil.copy()) na pasta do cliente. Simples assim!
