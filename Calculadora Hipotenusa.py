import math
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = math.hypot(co,ca)
print(f'A Hipotenusa vale {hi:.2f}')