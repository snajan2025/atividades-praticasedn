nome_produto = input("Digite o nome do produto: ")
valor = float(input("Digite o preço unitário do produto: "))
desconto_percentual = 20

valor_desconto = (valor * desconto_percentual) / 100
preco_final = valor - valor_desconto

print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {valor:.2f}")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")

