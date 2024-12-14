from random import randint
computador = randint(1, 10)
print("Acabei de pensar... num número de 0 a 10"
      "Será que você consegue adivinhar qual número eu pensei?")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite? "))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        print("ERRRROU!!")
print("ACERTOU MISERAVEL! com {} tentativas".format(palpite))
