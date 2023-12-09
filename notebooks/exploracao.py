
import json
import csv
import unicodedata # importando a biblioteca unicodedata para remover os acentos


# 1 -> Lendo arquivos JSON e CSV e transformando em um dicionário ambos os arquivos


# armazena o caminho do arquivo json em uma variável
path_json = 'pipeline_dados_Py\data_raw\dados_empresaA.json'

# MANEIRA DE LER COMO SE EU TIVESSE NO TEAMS E NAO ENVIASSE COMO CÓDIGO, AI NAO FICA NO FORMATO DO DADO CORRETO A PARTIR DAQUELE ARQUIVO
# o with é usado para abrir e fechar o arquivo, o 'r' é para ler o arquivo, o arquivo só fica aberto enquanto há comando dentro do with o 'as' é para dar um nome ao arquivo, funciona
# como um apelido, o file é o apelido que eu dei ao arquivo, o readline é para ler a primeira linha do arquivo de forma desestruturada, ou seja, não fica no formato do arquivo
with open(path_json, 'r') as file: 
    print("Leitura do arquivo ->", file.readline())
# guardando o resultado em uma variável
    dados = file.readline()

# agora vamos transformar o resultado em um dicionário.
# explicando oq é um dicionario: é um tipo de dado que tem uma chave e um valor, a chave é o nome da variável e o valor é o valor da variável, é como se fosse uma lista, 
# mas ao invés de ter um índice, ele tem uma chave, que pode ser qualquer coisa, pode ser um número, uma string, etc.
# usando isso conseguimos acessar os dados de forma mais fácil, pois não precisamos saber o índice, só precisamos saber a chave.
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
        # print("Leitura do arquivo ->", dados_json)
        print(dados_json[0])

# Agora faremos a mesma coisa, mas com o arquivo csv
path_csv = 'pipeline_dados_Py\data_raw\dados_empresaB.csv'
dados_csv = []

with open(path_csv, 'r') as file_csv:
    # print(file_csv.readlines())
    dados_csv = (file_csv.readlines())

print(dados_csv[1][0])


# agora vamos ler o arquivo csv com o csv.reader, ele é um método que lê o arquivo csv e transforma em um objeto, que é um tipo de dado que tem uma estrutura.
with open(path_csv, 'r') as file_csv:
# spamreader é o nome do objeto que vai ser criado, o csv.reader é o método que vai ler o arquivo csv, o delimiter é o delimitador, ou seja, o que separa os dados, no caso é a vírgula.
    spamreader = csv.reader(file_csv, delimiter=',')

# Percorrer as linhas do arquivo CSV e a variável row representa cada linha do arquivo durante cada iteração do loop
    for row in spamreader:
# o código abaixo está removendo os acentos das palavras, pois o python não consegue ler acentos, então ele vai remover os acentos e transformar em utf-8, que é o formato que o python consegue ler.
# usei a funcao unicodedata.normalize para remover os acentos, o NFKD é um formato de unicode, o encode é para codificar o texto, o ASCII é o formato que o python consegue ler, o ignore é para ignorar os caracteres que não são ASCII, o decode é para decodificar o texto.
        normalized_row = [unicodedata.normalize('NFKD', cell).encode('ASCII', 'ignore').decode('utf-8') for cell in row]
        dados_csv.append(normalized_row)  # o código está imprimindo a variável row, que representa uma linha do arquivo CSV.

# print(type(dados_csv)) # tipo de dado do csv
# print(type(dados_json)) # tipo de dado do json

# agora vamos fazer a mesma coisa, mas com o DictReader, que é um método que lê o arquivo csv e transforma em um dicionario.
dados_csv = []
with open(path_csv, 'r') as file_csv:
    spamreader = csv.DictReader(file_csv, delimiter=',')
    for row in spamreader:
        normalized_row = [unicodedata.normalize('NFKD', cell).encode('ASCII', 'ignore').decode('utf-8') for cell in row]
        dados_csv.append(normalized_row)

print(dados_csv[0])

#2 -> leitura ou extração de dados