# Atividade Prática 02 
valor_reais = float(input("Digite o valor em reais (R$): "))

cotacao_dolar = 5.37

cotacao_euro = 6.25

valor_dolar = valor_reais / cotacao_dolar

valor_euro = valor_reais / cotacao_euro

print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Valor em dólares: $ {valor_dolar:.2f}")
print(f"Valor em euros: € {valor_euro:.2f}")