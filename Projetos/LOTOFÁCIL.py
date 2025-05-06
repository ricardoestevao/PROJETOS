# Programa que irar sortear para o usuário 15 números dentre 1 ao 25 para jogar na LOTOFÁCIL. 
from random import randint
from time import sleep
print('-=-' * 20)
print('           SORTEANDO NÚMEROS LOTOFÁCIL          ')
print('-=-' * 20)
lista = list()
jogos = list()
quant = int(input('Quantos jogos você deseja que sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 25)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 15:
                break
    lista.sort() 
    jogos.append(lista[:])       
    lista.clear()
    tot += 1
print('-=-' * 3, f' SORTEANDO {quant} JOGOS', '-=-' * 3)
for i, l in enumerate(jogos):
        print(f'Jogo {i+1}: {l}')
        sleep(1)