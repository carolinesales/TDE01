#Faça um algoritmo que dado um horário fornecido pelo usuário (hora, minutos e segundos)
# calcule o total de minutos e o total de segundos que transcorreram desde o início do dia.

print("Bem-vindo(a) a nossa Calculadora, por favor Informe os dados atuais")
hora = int(input("Hora: "))
minuto = int(input("Minuto: "))
segundos = int(input("Segudos: "))

minutoSegundos = minuto * 60
horaMinuto = hora * 60
horaSegundos= horaMinuto * 60
calculoSegundos = segundos + minutoSegundos + horaSegundos
calculoMinutos = horaMinuto + minuto

print("O total de minutos que transcorrem desde o inicio do dia é: ", calculoMinutos)
print("O total de segundos que transcorreram desde o inicio do dia é: ", calculoSegundos)
