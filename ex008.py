#Conversor de Medidas
distM = int(input('Uma distância em metros: '))
km = distM / 1000
hm = distM / 100
dec = distM / 10
drs = distM * 10
cm = distM * 100
mm = distM * 1000
print(f'A medida de {distM:.1f}m corresponde a')
print(f'{km}km')
print(f'{hm}hm')
print(f'{dec}dam')
print(f'{drs}dm')
print(f'{cm}cm')
print(f'{mm}mm')
