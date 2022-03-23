#Reajuste Salarial
sal = float(input('Qual o saário do Funcionário? R$'))
aumento = sal + (sal * 15 / 100)
print(f'Um funcionário que ganhava R${sal:.2f}, com 15% de aumento, passa a receber R${aumento:.2f}')