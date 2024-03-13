from random import randint
from time import sleep
print('Olá Mundo!')
itens = (' Pedra ', 'Papel' , 'Tesoura')
computador = randint(0,2)
print('''\033[31m Suas Opções 
      [ 0 ] - Pedra 
      [ 1 ] - Papel 
      [ 2 ] - Tesoura ''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !!!')
print('-=' * 14)
print('Computador Jogou {}'.format(itens[computador]))
print('Jogador Jogou {}'.format(itens[jogador]))
print('-=' * 14)
if computador == 0:
    if jogador == 0:
        print('EMPATE !!')
    elif jogador == 1:
        print('JOGADOR VENCEU !!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU !!')
    else:
        print('=-= JOGADA INVÁLIDA =-=')
if computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU !!')
    elif jogador == 1:
        print('EMPATE !!')
    elif jogador == 2:
        print('JOGADOR VENCEU !!')
    else:
        print('=-= JOGADA INVÁLIDA =-=')
if computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU !!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU !!')
    elif jogador == 2:
        print('EMPATE !!')
    else:
        print('=-= JOGADA INVÁLIDA =-=')
