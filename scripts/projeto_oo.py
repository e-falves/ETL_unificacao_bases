import json
import csv

class Dados:
    def __init__(self, path):
        self.path = path

    def leitura_json(self):
        with open(self.path, 'r') as file:
            dados = json.load(file)
        return dados
    
    def leitura_csv(self):
        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.reader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv
    
    def correcao_coluna(self, rename_columns):
        novo_nome = []
        antigo = self[0]
        for nome in antigo:
            valor = rename_columns.get(nome, nome)
            novo_nome.append(valor)
        self[0] = novo_nome
        return self
    
    @staticmethod
    def list_to_dict(lista):
        if not lista or not isinstance(lista, list):
            raise ValueError('O argumento deve ser uma lista não vazia.')
        keys = lista[0]
        values = lista[1:]
        return [dict(zip(keys, v)) for v in values]

    @staticmethod
    def agregacao(dadosA, dadosB, formato):
        if isinstance(dadosA, formato) != isinstance(dadosB, formato):
            raise ValueError('Arquivos de formato diferente.')
        dados_agregados = []
        dados_agregados.extend(dadosA)
        dados_agregados.extend(dadosB)
        return dados_agregados
    
    @staticmethod
    def tabela(dados, rename_columns):
        dados_tabela = [list(rename_columns.values())]
        for dic in dados:
            valores = []
            for key in rename_columns.values():
                valor = dic.get(key, "Indisponível")
                valores.append(valor)
            dados_tabela.append(valores)
        return dados_tabela

    @staticmethod
    def salvar(path, dados):
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(dados)
        print(path)