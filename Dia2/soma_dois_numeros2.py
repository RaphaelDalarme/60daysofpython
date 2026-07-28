def somar(numero1, numero2):
    somar = numero1 + numero2
    print("A soma dos dois números é:", somar)
    return somar

somar(5, 10)

def somar_dois_numeros():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    somar(numero1, numero2)

somar_dois_numeros()