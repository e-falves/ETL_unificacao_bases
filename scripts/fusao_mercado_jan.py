from projeto_oo import Dados

#Leitura 
path_csv = '/home/everton_pc/projeto2/pipeline_dados/data_raw/dados_empresaB.csv'

path_json = '/home/everton_pc/projeto2/pipeline_dados/data_raw/dados_empresaA.json'

dados_empresaA = Dados(path_json)
dados_empresaA = dados_empresaA.leitura_json()
print(f'Dados empresaA: {dados_empresaA[0]}')

dados_empresaB = Dados(path_csv)
dados_empresaB = dados_empresaB.leitura_csv()
print(f'Dados empresaB: {dados_empresaB[0]}')

#Transformação
rename_columns = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

dados_empresaB = Dados.correcao_coluna(dados_empresaB,rename_columns)
print(f'Novos dados empresaB: {dados_empresaB[0]}')

dados_empresaB = Dados.list_to_dict(dados_empresaB)
print(f'Novo formato empresaB: {dados_empresaB[0]}')

dados_agregados = Dados.agregacao(dados_empresaA, dados_empresaB, list)
print(f'Dados agregados L0: {dados_agregados[0]}')
print(f'Dados agregados L-1: {dados_agregados[-1]}')

dados_tabulares = Dados.tabela(dados_agregados, rename_columns)
print(f'Tabela final L0: {dados_tabulares[1]}')
print(f'Tabela final L-1: {dados_tabulares[-1]}')

# Salvamento
path_tabela = 'data_processed/data_agregados.csv'

Dados.salvar(path_tabela, dados_tabulares)

