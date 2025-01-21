import random
import time
import operator
game = {'player1' : random.randint(1, 6),
    'player2' : random.randint(1, 6),
    'player3' : random.randint(1, 6),
    'player4' : random.randint(1, 6)}
ranking = list()
print('drawn values: ')
for k, v in game.items():
    print(f'{k} --> {v}')
    time.sleep(1)
ranking = sorted(game.items(), key=operator.itemgetter(1), reverse=True)
print('RAKING')
for i, v in enumerate(ranking):
    print(f'   {i+1}° : {v[0]} with number {v[1]}.')
    time.sleep(1)
print("Bye Bye")
