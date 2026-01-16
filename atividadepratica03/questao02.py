def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"
        
    return imc, classificacao

p = float(input("Digite o peso (kg): "))
a = float(input("Digite a altura (m): "))

valor_imc, status = calcular_imc(p, a)

print(f"Seu IMC é {valor_imc:.2f} e sua classificação é: {status}")