#Analisador de Textos
from time import sleep
nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o seu nome....')
sleep(2)
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minusculas é {nome.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))