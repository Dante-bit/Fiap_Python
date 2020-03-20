data = str(input("Qual seu tipo de graduação (Tecnologo ou Bacharelado)?")).upper().strip()
if data != "TECNOLOGO" and data != "BACHARELADO":
    print("Escreva uma das opções!")
elif data == "TECNOLOGO":
        print("2 até 3 anos")
else:
     print("4 até 6 anos")

