print("-"*12, "Calculadora financeira", "-"*12)
aplicação = float(input("Qual o valor da sua aplicação(Sem aportes)? R$"))
Taxa = float(input("Qual a taxa de juros atual?(Anuel e em %) "))
mes1 = aplicação + (aplicação*(Taxa/12)/100)
print("Em um mês se tornara ", mes1)
ano1 = aplicação + (aplicação*Taxa/100)
print("Em um ano se tornara", ano1)
ano5 = aplicação * (1+Taxa/100)**5
print("Em 5 anos se tornara {:.2f}".format(ano5))