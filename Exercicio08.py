#Construa um algoritmo que calcule a quantidade de latas de tinta necessárias e o custo para pintar tanques
#cilíndricos de combustível, em que são fornecidos a altura e o raio desse cilindro. Sabendo que:

#a. A lata de tinta custa R$ 50,00;
#b. Cada lata contém 5 litros;
#c. Cada litro de tinta pinta 3 metros quadrados;
#d. Entradas: altura e raio;
#e. Saída: custo em R$ e quantidade de latas.

altura = float(input("Informe a altura do cilindro do Tanques de Combustivel: "))
raio = float(input("Informe o raio do cilindro do Tanque de Combustivel: "))

calculoAreaCilindro = 2 * 3.14 * raio * (raio + altura)
quantidadeLatas = (calculoAreaCilindro / 3) / 5
valorTotal = quantidadeLatas * 50

print("A quantidade de latas de tinta necessárias é de: ", quantidadeLatas)
print("O Custo total será: ", valorTotal)