#Sorteando uma ordem na lista
from random import shuffle
primeiro = str(input('Primeiro aluno: '))
segundo = str(input('Segundo aluno: '))
terceiro = str(input('Terceiro aluno: '))
quarto = str(input('Quarto aluno: '))
lista = [primeiro, segundo, terceiro, quarto]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)