#Escreva um algoritmo que leia o ano de nascimento de uma pessoa, calcule e mostre a idade que completará em 2032.

anoNascimento = int(input("Informe seu ano de Nascimento: "))

calculoIdade = 2032 - anoNascimento
print("Sua idade em 2032 será: " + str(calculoIdade), "anos")