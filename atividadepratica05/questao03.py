def calcular_desconto(valor_produto, porcentagem_desconto):
    
    desconto = valor_produto * (porcentagem_desconto / 100)
    valor_final = valor_produto - desconto
    return valor_final

valor = float(input("Digite o valor do produto: "))
porcentagem = float(input("Digite a porcentagem de desconto: "))

resultado = calcular_desconto(valor, porcentagem)

print(f"O valor com desconto é de {resultado:.2f}")