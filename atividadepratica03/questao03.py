def converter_temperatura(valor, origem, destino):

    if origem == "C":
        celsius = valor
    elif origem == "F":
        celsius = (valor - 32) / 1.8
    elif origem == "K":
        celsius = valor - 273.15
        
    if destino == "C":
        return celsius
    elif destino == "F":
        return celsius * 1.8 + 32
    elif destino == "K":
        return celsius + 273.15

temp = float(input("Digite a temperatura: "))
de = input("Unidade de origem (C, F, K): ").upper()
para = input("Converter para (C, F, K): ").upper()

resultado = converter_temperatura(temp, de, para)
print(f"A temperatura convertida é: {resultado:.2f} {para}")