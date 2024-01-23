from django.test import TestCase

from aluraflix.models import Programa


class ProgramaModelTestCase(TestCase):
    def setUp(self):
        self.programa = Programa(
            titulo="Titulo do Programa 1",
            data_lancamento="2003-01-01",
        )

    def test_verifica_atributos_do_programa(self):
        """Teste que verifica os atributos default do programa"""
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)
        self.assertEqual(self.programa.tipo, "F")
