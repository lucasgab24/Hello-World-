# Criar lista vazia
valores = []

# Ler 5 valores e armazenar na lista
for i in range(5):
    valores.append(int(input(f"Digite o {i+1}º valor: ")))

# Encontrar maior e menor valor
maior = max(valores)
menor = min(valores)

# Encontrar posições do maior e menor valor
posicoes_maior = [i+1 for i, x in enumerate(valores) if x == maior]
posicoes_menor = [i+1 for i, x in enumerate(valores) if x == menor]

# Imprimir resultados
print("\nValores digitados:", valores)
print(f"Maior valor: {maior} (posições: {posicoes_maior})")
print(f"Menor valor: {menor} (posições: {posicoes_menor})")

frutas = ['maçã', 'banana', 'laranja']
for i, fruta in enumerate(frutas):
 print(f"{i}: {fruta}")

palavra = "Python"
for i, letra in enumerate(palavra):
 print(f"{i}: {letra}")
 
numeros = [1, 2, 3, 4, 5]
for i, numero in enumerate(numeros, start=1):
 print(f"{i}: {numero}")
