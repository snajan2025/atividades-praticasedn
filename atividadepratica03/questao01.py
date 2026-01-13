idade = int(input("Digite a sua idade: "))

if idade < 0:
    print("Idade invalida:")
elif idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")



