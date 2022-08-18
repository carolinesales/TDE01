#Construa um algoritmo que leia o valor do salário de um determinado funcionário e calcule
# quantos salários-mínimos este funcionário recebe.

salario = float(input("Informe seu Salario: "))

salarioMinimo = 1200
calculoSalario = salario / salarioMinimo

print("Você recebe: ", str(calculoSalario), "minimos")

