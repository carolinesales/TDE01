#Elabore um algoritmo que leia o preço de um produto e então mostre
#quais os valores em: 3 parcelas com 5% de juros, 2 parcelas sem juros e
#o preço à vista com 5% de desconto.

precoProduto = float(input("Informe o valor do Produto:  "))

juros = precoProduto * 0.05
valorComJuros = (precoProduto + juros)/3
valorParcelado = precoProduto/2
ValorComDesconto = precoProduto - juros

print("Parcelamento em 3 vezes com 5% de juros: ", valorComJuros)
print("Parcelamento em 2 vezes sem juros: ", valorParcelado)
print("A vista com 5% de desconto: ", ValorComDesconto)