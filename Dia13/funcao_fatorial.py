def fatorial(n):
    """
    Calcula o fatorial de um número usando recursão

    :param n: Número inteiro não negativo:
    :return: Fatorial de n.
    """

    if n < 0:
        raise ValueError("O numero deve ser positivo")

    if n == 0 or n == 1:
        return 1

    #recursividade
    return n * fatorial(n - 1)

#print(fatorial(15))

try:
    print(f"Fatorial igual a {fatorial(15)}")
except ValueError as e:
    print(e)
