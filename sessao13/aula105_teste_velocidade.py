"""
# Exemplo 01

def nums():
    for num in range(1, 10):
        yield num

ge1 = nums()

print(ge1)
print(next(ge1))
print(next(ge1))

ge2 = (num for num in range(1, 10))

print(ge2)
print(next(ge2))
print(next(ge2))

"""
import time

gen_inicio = time.time()
print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio

list_inicio = time.time()
print(sum([num for num in range(100000000)]))
list_tempo = time.time() - list_inicio

print(gen_tempo)
print(list_tempo)









