name = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))

risco = input("Você é do grupo de risco? (SIM ou NAO): ").upper()


if risco != 'SIM' and risco != 'NAO':
    risco = input("Você é do grupo de risco? (SIM ou NAO): ").upper()

else:
    if idade < 15 or idade > 60:
        print("Partiu Itália")
    elif idade > 60:
        print("Sua idade esta nas pessoas mais afetadas: ", idade)
    elif risco == "SIM":
        print("Ai minhas asma")
    else:
        print("Partil praia")
