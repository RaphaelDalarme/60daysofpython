import random
import string 

#string fornece um conjunto de caracteres prontos

def gerar_senha(tamanho):
    comprimento = tamanho
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''

    while len(senha) < comprimento:
        senha += random.choice(caracteres)

    print(f"Sua senha ficou assim: {senha}")

print(gerar_senha(8))