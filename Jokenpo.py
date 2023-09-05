# Pedra Papel e Tesoura

from random import randint # Importa a biblioteca de Randomizer
from time import sleep # Importa a biblioteca de timer

itens = ('Pedra', 'Papel', 'Tesoura') # Cria uma lista de itens
computador = randint(0, 2) # Faz o computador sortear do elemento 0 da lista até o elemento 2 da lista

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PEPEL
[ 2 ] TESOURA\n''')

jogador = int(input('Qual é sua jogada? ')) # Pergunta ao usuário qual será a sua jogada
if jogador > 2: # Caso o usuário venha a escolher um número maior que o número de elementos na lista, o progama para de executar
    print('\nJogada Invalida! Tente novamente.')
    exit() # Stop
    
print("\nJO")
sleep(1)
print("KEN")
sleep(1)
print("PO!\n")

print('-=' * 11) # Mostra na tela os resultados da escolha do usuário e do computador (Randomizada)
print(f'O Computador jogou {itens[computador]}')
print(f'O Jogador jogou {itens[jogador]}')
print('-=' * 11)

if computador == 0:  # Computador jogou Pedra
    if jogador == 0: # Jogador jogou Pedra
        print('\nEMPATE!')
    elif jogador == 1: # Jogador jogou Papel
        print('\nJogador VENCEU!')
    elif jogador == 2: # jogador jogou Tesoura
        print('\nComputador VENCEU!')
        
elif computador == 1:  # Computador jogou Papel
    if jogador == 0: # Jogador jogou Pedra
        print('\nComputador VENCEU!')
    elif jogador == 1: # Jogador jogou Papel
        print('\nEMPATE!')
    elif jogador == 2: # jogador jogou Tesoura
        print('\nJogador VENCEU!')
        
elif computador == 2:  # Computador jogou Tesoura
    if jogador == 0: # Jogador jogou Pedra
        print('\nJogador VENCEU!')
    elif jogador == 1: # Jogador jogou Papel
        print('\nComputador VENCEU!')
    elif jogador == 2: # jogador jogou Tesoura
        print('\nEMPATE!')
