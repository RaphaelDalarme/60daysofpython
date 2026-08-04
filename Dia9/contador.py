def contador_personalizado():
    try:
        limite = int(input("Digite o valor máximo do contador: "))
        limite += 1
        for i in range(limite):
            print(i)
            if i == limite:
                print("Contagem concluída!")
                break
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

contador_personalizado()