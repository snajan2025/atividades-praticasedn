import pandas as pd

def procesar_logs_treinamento(arquivo_log):
    try:
        leitor = pd.read_csv(arquivo_log)
        media = leitor['tempo_execucao'].mean()
        desvio_padrao = leitor['tempo_execucao'].std()
        return f"Media: {media:.2f}, Desvio Padrão: {desvio_padrao:.2f}"
    

    except FileNotFoundError:
        return "Arquivo não encontrado"
    

arquivo = input("Digite o nome do arquivo de log: ")
print (procesar_logs_treinamento("logs_treinamento.csv"))