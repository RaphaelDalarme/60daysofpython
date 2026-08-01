#frutas = ["banana", "maçã", "laranja", "uva", "abacaxi"]

#for fruta in frutas:
#    print(fruta)


#utilizando input para adicionar frutas à lista
nova_fruta = input("Digite o nome de uma fruta para adicionar à lista: ")

frutas = []

while True:
    fruta= input("Digite o nome de uma fruta para adicionar à lista (ou digite 'sair' para encerrar): ")
    if fruta == "sair":
        break
    frutas.append(fruta)

print("Lista de frutas atualizada:")
for fruta in frutas:
    print(fruta)