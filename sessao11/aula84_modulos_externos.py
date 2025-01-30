"""
# Exemplo 01 - colorama - Impressão de textos coloridos no terminal

from colorama import init, Fore

init()

print(Fore.MAGENTA + 'olá')

"""
import pydf

pdf = pydf.generate_pdf('<h1>Richard Gay</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
