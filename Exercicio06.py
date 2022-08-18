#Escreva um algoritmo que leia o valor de dois catetos de um triângulo retângulo e calcule a hipotenusa.

cateto01 = float(input("Informe o valor do Primeiro Cateto: "))
cateto02 = float(input("Informe o valor do Segundo Cateto: "))

calculo = ((cateto01 ** 2) + (cateto02 ** 2)) ** 0.5

print("O resultado do calculo é:  " + str(calculo))