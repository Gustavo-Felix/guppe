# Exemplo 01

from io import StringIO

mensagem = 'Mesnagem normal!'

arquivo = StringIO(mensagem)

print(arquivo.read())