#Sorteando um item na lista
from random import choice
primeiro = str(input('Primeiro aluno: '))
segundo = str(input('Segundo aluno: '))
terceiro = str(input('Terceiro aluno: '))
quarto = str(input('Quarto aluno: '))
lista = [primeiro, segundo, terceiro, quarto]
ran = choice(lista)
print(f'O aluno escolhido foi {ran}')