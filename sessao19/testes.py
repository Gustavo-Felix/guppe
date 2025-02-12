import unittest

from atividades import comer, dormir, engracada


class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """
        Testando se a comida é saudável
        """
        self.assertEqual(
            comer('Quiabo', True),
            'Estou comendo Quiabo por que me mantem em forma.'
        )

    def test_comer_gostosa(self):
        self.assertEqual(
            comer('Pizza', False),
            'Estou comendo Pizza por que só se vive uma vez.'
        )

    def test_dormir_pouco(self):
        self.assertEqual(
            dormir(4),
            'Continuo Cansado.'
        )

    def test_dormir_muito(self):
        self.assertEqual(
            dormir(10),
            'Descansei muito bem.'
        )

    def test_engracada(self):
        # self.assertEqual(engracada('Sergio Malandro'), False)
        self.assertFalse(engracada('Sergio Malandro'))
        self.assertTrue(engracada('Jim Carrey'), f'Jim Carrey deveria ser engraçado.')


if __name__ == '__main__':
    unittest.main()