#Catetos e Hipotenusa
from math import hypot
catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
hi = hypot(catetoOposto, catetoAdjacente)
#hi = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')