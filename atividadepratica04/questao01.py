while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Erro: divisão por zero.")
                continue
        else:
            raise ValueError("Operação inválida")

        print(f"O resultado é {resultado}")
        break  # sai do while se deu tudo certo

    except ValueError:
        print("Erro: digite valores válidos e uma operação correta.")
