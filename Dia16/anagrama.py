def anagrama(palavra1, palavra2):
    """
    Verifcar se duas palavras são um anagrama ou não

    :param palavra1: Primeira palavra
    :param palavra2: Segunda palavra
    :return: True se as palavras forem anagrama
    """
    #Removendo espaços e convertendo para letras minúsculas
    palavra1 = palavra1.replace(" ","").lower()
    palavra2 = palavra2.replace(" ","").lower() 

    if sorted(palavra1) == sorted(palavra2):
        return f"Essas palavras são anagramas"
    return f"Essas palavras não são anagramas"

print(anagrama("amor", "roma"))
