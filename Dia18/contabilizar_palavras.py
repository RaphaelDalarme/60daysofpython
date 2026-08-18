def contar_palavras(texto):
    """
    Contar palavras em um string
    :param texto:   String de entrada
    :return: Numero de palavras
    """

    palavras = texto.split()

    return len(palavras)

print(contar_palavras("oi tudo bem, como vai você?"))