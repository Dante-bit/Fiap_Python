access = input("Digite o seu nível de acesso (ADM, USR, GUEST): ").upper()
if access != "ADM" and access != "USR" and access != "GUEST":
    print("Olá desconhecido.")
elif access == "GUEST":
    print("Olá visitante.")
else:
    genre = input("Digite seu sexo (M ou F): ").upper()

    if genre != "M" and genre != "F":
        print("Digite seu sexo corretamente.")
    else:
        if genre == "M" and access == "ADM":
            print("Olá administrador.")
        elif genre == "F" and access == "ADM":
            print("Olá admiministradora.")
        elif genre == "M" and access == "USR":
            print("Olá usuário.")
        elif genre == "F" and access == "USR":
            print("Olá usuária.")
        else:
            print("Olá desconhecido.")