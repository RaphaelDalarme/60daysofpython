def transpor_matriz(matriz):
    """ 
    Gerar uma matriz transposta de 3x3
    Substitui colunas horizontais por verticais

    Arg: Matriz que vão lista de 3 numeros na horizontal e vertical
    Return: Matriz transposta
    Raises: ValueError: Se a matriz não ter 3x3
    """

    if len(matriz) != 3 or not all(len(linha) == 3 for linha in matriz):
        raise ValueError("A matriz não possui o tamanho 3x3")

    transposta = [[matriz[j][i] for j in range(3)] for i in range(3)]

matriz = [
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , 8 , 9]
]

transposta = []

for i in range(3):
    nova_linha = []

    for j in range(3):
        nova_linha.append(matriz[j][i])

    print(nova_linha)
