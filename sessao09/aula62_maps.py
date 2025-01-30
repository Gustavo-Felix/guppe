"""
import math

def area(r):
    # Retorna a a área do circulo de acordo com o raio ('r')
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2.2, 3, 10, 8, 44, 10]

# Forma comum

areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 02 - map

areas = map(area, raios)
print(list(areas))

# Forma 03 - Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS-map: Após o primeiro uso, ele zera
"""

# Para Fixar - Map

cidades = [('Berlim', 29), ('Cairo', 36), ('Los angeles', 26), ('Tokyo', 27)]

print(cidades)

conversao = lambda c: (c[0], (9 / 5) * c[1] + 32)

print(list(map(conversao, cidades)))


















