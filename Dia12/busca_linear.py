def busca_linear(lista, numero_procurado):
    """
    Procurar um numero dentro de uma lista utilizando busca linear

    :param lista:lista de numeros
    :param numero_procurado: o numero que procurar
    """

    for i, numero in enumerate(lista):  
        if numero == numero_procurado:
            return i 
    return -1

lista = ["raphael", 0, 20, 8, 11, "joão"]
numero_procurado = 20
buscando_numero = busca_linear(lista, numero_procurado)
print(buscando_numero)

if buscando_numero != -1:
    print(f"O número se encontra no indice: {buscando_numero}")
