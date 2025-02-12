# Exemplo 01 - unittest - hooks
# Hooks são os testes em si
# setup() -> Executado antes de cada módulo de teste
# tearDown() -> Executado no final de cada módulo de teste

import unittest

class ModuloTeste(unittest.TestCase):

    def setUp(self):
        pass

    def test_primeiro(self):
        pass

    def test_segundo(self):
        pass

    def tearDown(self):
        pass