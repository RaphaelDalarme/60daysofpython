entrada = input("Digite um número inteiro: ")

try:
    numero = int(entrada)
    if numero % 2 == 0:
        print(f"O número {numero} é par.")      
    else:
        print(f"O número {numero} é ímpar.")

except ValueError:
    print("Erro: Por favor, digite um número inteiro válido.")