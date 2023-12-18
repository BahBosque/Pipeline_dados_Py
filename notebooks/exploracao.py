
import json
import csv
import unicodedata # importando a biblioteca unicodedata para remover os acentos


# 1 -> Lendo arquivos JSON e CSV e transformando em um dicionário ambos os arquivos


# armazena o caminho do arquivo json em uma variável
path_json = 'data_raw\dados_empresaA.json'

# MANEIRA DE LER COMO SE EU TIVESSE NO TEAMS E NAO ENVIASSE COMO CÓDIGO, AI NAO FICA NO FORMATO DO DADO CORRETO A PARTIR DAQUELE ARQUIVO
# o with é usado para abrir e fechar o arquivo, o 'r' é para ler o arquivo, o arquivo só fica aberto enquanto há comando dentro do with o 'as' é para dar um nome ao arquivo, funciona
# como um apelido, o file é o apelido que eu dei ao arquivo, o readline é para ler a primeira linha do arquivo de forma desestruturada, ou seja, não fica no formato do arquivo
with open(path_json, 'r') as file: 
    #print("Leitura do arquivo JSON ->", file.readline())
# guardando o resultado em uma variável
    dados = file.readline()

# agora vamos transformar o resultado em um dicionário.
# explicando oq é um dicionario: é um tipo de dado que tem uma chave e um valor, a chave é o nome da variável e o valor é o valor da variável, é como se fosse uma lista, 
# mas ao invés de ter um índice, ele tem uma chave, que pode ser qualquer coisa, pode ser um número, uma string, etc.
# usando isso conseguimos acessar os dados de forma mais fácil, pois não precisamos saber o índice, só precisamos saber a chave.
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
        # print("Leitura do arquivo ->", dados_json)
        #print(dados_json[0])

# Agora faremos a mesma coisa, mas com o arquivo csv
path_csv = 'data_raw\dados_empresaB.csv'
dados_csv = []

with open(path_csv, 'r') as file_csv:
    # print(file_csv.readlines())
    dados_csv = (file_csv.readlines())

#print(dados_csv[1][0])


# agora vamos ler o arquivo csv com o csv.reader, ele é um método que lê o arquivo csv e transforma em um objeto, que é um tipo de dado que tem uma estrutura.
with open(path_csv, 'r', encoding='utf-8-sig') as file_csv:
# spamreader é o nome do objeto que vai ser criado, o csv.reader é o método que vai ler o arquivo csv, o delimiter é o delimitador, ou seja, o que separa os dados, no caso é a vírgula.
    spamreader = csv.reader(file_csv, delimiter=',')

# Percorrer as linhas do arquivo CSV e a variável row representa cada linha do arquivo durante cada iteração do loop
    for linha in spamreader:
        dados_csv.append(linha)  # o código está imprimindo a variável row, que representa uma linha do arquivo CSV.

# print(type(dados_csv)) # tipo de dado do csv
# print(type(dados_json)) # tipo de dado do json

# agora vamos fazer a mesma coisa, mas com o DictReader, que é um método que lê o arquivo csv e transforma em um dicionario.
dados_csv = []
with open(path_csv, 'r', file_csv='utf-8-sig') as file_csv:
    spamreader = csv.DictReader(file_csv, delimiter=',')
    for linha in spamreader:
        dados_csv.append(linha)

#print(type(dados_csv))

#2 -> leitura ou extração de dados

# 2.1 -> substituição de chave para chave unica

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

#print(key_mapping)

new_data_csv = []

# o código abaixo está percorrendo o dicionário dados_csv, para substituir sua antiga chave para a atual que é a mesma dos dados_json
for old_dict in dados_csv:
    dict_temp = {} # para cada dicionario no dados_csv, ele cria um dicionario vazio
    for old_key, value in old_dict.items(): # para cada chave e valor no dicionario antigo, usando a função 'items' ele acessa cada chave e valor do old_dict
        dict_temp[key_mapping[old_key]] = value
    new_data_csv.append(dict_temp) # adiciona o dicionario temporario no new_data_csv

#print(new_data_csv[0])

# 3 -> JUNCAO DOS DADOS: Primeiro verificamos a quantidade de registro em cada arquivo, depois juntamos os dois arquivos em um só

#print(len(dados_json))
#print(len(new_data_csv))

# agora vamos juntar os dois arquivos em um só, para isso vamos usar o método extend, que é um método que adiciona um elemento no final da lista, mas ele adiciona um elemento iterável, ou seja, adiciona uma lista dentro de outra lista.

combined_list = [] #primerio criamos uma lista vazia

combined_list.extend(dados_json) #usamos o metodo extend para adicionar os dados_json na lista vazia
combined_list.extend(new_data_csv) #fazemos o mesmo com os dados_csv

print(combined_list[0])

#OBSERVAÇÃO: o metodo extend nao olha a quantidade de elementos, ele apenas adiciona um elemento iteravel no final da lista, ou seja, ele adiciona uma lista dentro de outra lista, por isso que é necessário ter atenção para quantidade de colunas e as informações serem iguais, pois se não for, ele vai adicionar os dados de forma errada.

#4 -> SALVAR OS DADOS

caminho_dados_combinos = 'data_processed\dados_combinados.csv'
nome_colunas = combined_list[0].keys() # o método keys retorna as chaves do dicionário, ou seja, ele retorna o nome das colunas.

# agora vamos salvar os dados em um arquivo csv, para isso vamos usar o método DictWriter, que é um método que escreve um arquivo csv a partir de um dicionário.
with open(caminho_dados_combinos, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file, fieldnames=nome_colunas)
    writer.writeheader() # o método writeheader escreve o cabeçalho do arquivo csv, ou seja, escreve o nome das colunas.

# o código abaixo está percorrendo a lista combined_list e escrevendo cada linha no arquivo csv.
    for row in combined_list:
        writer.writerow(row)