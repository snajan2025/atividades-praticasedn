def eh_bissexto(ano):

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

ano_usuario = int(input("Digite um ano para verificar: "))

if eh_bissexto(ano_usuario):
    print(f"O ano {ano_usuario} é bissexto!")
else:
    print(f"O ano {ano_usuario} não é bissexto.")