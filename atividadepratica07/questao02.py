import csv

def escrever_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Nome', 'Idade', 'Cidade'])
            for linha in dados:
                escritor.writerow(linha)
            return f"Dados escrito com sucesso no arquivo {nome_arquivo}"
        
    except Exception as e:
        return f"Erro ao escrever no arquivo: {e}"
    

dados = [
    ['Alberto', 48, 'Água Branca'],
    ['Bruna', 34, 'Belo Horizonte'],
    ['Carlos', 29, 'Curitiba']
]

nome_arquivo = input("Digite o nome do arquivo CSV: ")
print(escrever_csv(nome_arquivo, dados))