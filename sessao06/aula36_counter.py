"""

# Exemplo 01
lista = [1, 1, 1, 2, 3, 4, 5, 6, 2, 3, 3, 4]

res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 3, 3: 3, 2: 2, 4: 2, 5: 1, 6: 1})
# Para cada elemento da lista, o Counter colocou a quantidade de ocorrencias do valor

# Exemplo 02

print(Counter('Geek University'))

"""

from collections import Counter

# Exemplo 03

texto = """Tribalistas é o álbum de estreia e epônimo do supergrupo musical brasileiro Tribalistas. O seu lançamento ocorreu 
em 4 de novembro de 2002 através da editora discográfica independente Phonomotor, sob distribuição da EMI. 
Desde o início de suas carreiras, os músicos brasileiros Arnaldo Antunes, Carlinhos Brown e Marisa Monte 
estavam presentes nos trabalhos uns dos outros com certa frequência, mantendo também uma amizade pessoal. 
Em 2001, Monte foi convidada a contribuir com vocais em uma das faixas do quinto álbum de estúdio de Antunes, Paradeiro, que Brown estava produzindo em Salvador, Bahia. 
A passagem, que estava programada para durar apenas dois dias, acabou estendendo-se por uma semana. 
Neste período, eles compuseram 13 músicas de uma vez e, após um período discutindo o que fariam com cada uma delas, acordaram por registrá-las em conjunto. 
As gravações do projeto ocorreram entre 8 a 24 de abril de 2002 no estúdio projetado na casa de Monte, 
no Rio de Janeiro, sob a produção musical da própria cantora, a qual contou com o auxílio de Antunes, Brown e do músico Alê"""

palavras = texto.split()

res = Counter(palavras)

print(res)

# as 5 Palavras com mais ocorrencias
print(res.most_common(5))







