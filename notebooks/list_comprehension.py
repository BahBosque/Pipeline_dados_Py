import pandas as pd

caminho_csv = 'data_raw\dados_empresaB.csv'

dados_csv = pd.read_csv(caminho_csv, sep=',', encoding='utf-8-sig')

new_dados_csv = []

key_mapping = {'Nome do Item': 'Nome do Produto',    
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}


#new_dados_csv = [{key_mapping.get(old_key): value for old_key, value in old_dict.items()} for old_dict in dados_csv.iterrows()]

for index, linha in dados_csv.iterrows():
    new_dados_csv.append(
            {
                key_mapping.get(old_key): value 
                    for old_key, value in linha.items()
            }
                        )

print(new_dados_csv[0])