import unittest

from robo import Robo

class RoboTeste(unittest.TestCase):

    def setUp(self):
        print('Setup está sendo executado...')
        self.megaman = Robo('Mega-man', bateria=50)

    def test_carregar(self):
        self.megaman.carregar_bateria()
        self.assertEqual(self.megaman.bateria, 100), 'Erro ao carregar'

    def test_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), 'Meu nome é MEGA-MAN'), 'O nome está incorreto'
        self.assertEqual(self.megaman.bateria, 49), 'A bateria não reduziu'

    def test_aprender_habilidade(self):
        self.megaman.aprender_habilidade("Destruir Naves", 49)
        self.assertIn('Destruir Naves', self.megaman.habilidades)

    def tearDown(self):
        print('TearDown está sendo executado...')

if __name__ == '__main__':
    unittest.main()