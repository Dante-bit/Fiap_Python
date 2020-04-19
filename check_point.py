import re
lista = ["4984763422788047",
"4984536380706668",
"4984837056767236",
"4984104166805301",
"4984038800678155",
"4984706762337388",
"4984401166832743",
"4984428543545383",
"4984132155881264",
"4984025088585152",
"5288048633278438",
"5388448231308737",
"5528675871405560",
"5523022523845734",
"5150253362051320",
"5546601165637823",
"5818656121882088",
"5874843268374241",
"5084588166707374",
"5520621651848718",
"6027236688455787",
"6004727672440444",
"6007416865327637",
"6017410217676682",
"6030871216782628",
"6025571583730534",
"6054081270086533",
"6064156287045074",
"6086064774443055",
"6066182345534568",
]

print("\033[1;32m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\033[1;32m+              Bem VINDO AO PROGRAMA HACKER                   +")
print("\033[1;32m+ Programa desenvolvido APENAS PARA HACKERS QUE SABEM HACKEAR!+")
print("\033[1;31m+          Se voce for um professor não utilize-o!            +")
print("\033[1;32m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def search(lista):
    prof = input("Você é um professor? (S) ou (N): ").upper()
    if prof == "S":
        print("Professores não podem utilizar esse tipo de artefato!")
    elif prof == "N":

        while True:
            entrada = input("Digite seu CARTÃO DE CRÉDITO: ")
            if len(entrada) == 16:
                for i in lista:
                    if entrada == i:
                        print("Seu cartão se encontra na nossa base de dados")
                        print("Seu cartão de crédito FOI HACKEADO, HA HA, me dê nota 10 que devolverei seus dados!!")
                        
                        break
            else:
                for i in lista:
                    regex = re.search(entrada, i)
                    if regex:
                        print("Encontramos coisas parecidas, porém nao encontramos seu cartao >> " + i)
                                #print("HA HA HA, estamos adicionando seu cartão a nossa base de dados...")
                                #lista.append(entrada)
                                #print(i)
                            #if entrada == i:
                            #    print("Encontramos")
                            #    break
                    else:
                        print("Não encontramos nada!")
                        break

    else:
        print("Saia, você é um IMPOSTOR!")
search(lista)