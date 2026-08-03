def pode_dirigir(idade):
    if idade >= 18:
        return "Você pode dirigir"
    else:
        return "Você não pode dirigir"

try:
    idade = int(input("Digite sua idade: "))
    print(pode_dirigir(idade))
except ValueError:
    print("Por favor, insira um número válido para a idade.")