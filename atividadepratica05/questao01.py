def calcular_gorjeta(valor_conta, porcentagem_gorjeta):

    valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return valor_gorjeta

valor = float(input("Digite o valor total da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10): "))

resultado = calcular_gorjeta(valor, porcentagem)

print(f"O valor da gorjeta a ser deixada é de R$ {resultado:.2f}")