from django.test import TestCase

from aluraflix.models import Programa


class FixturesTestCase(TestCase):
    fixtures = ["programas_iniciais"]

    def test_verifica_se_existem_programas_na_base(self):
        """ "Teste que verifica se existem programas na base de dados"""
        self.assertTrue(Programa.objects.exists())

        coisas_bizarras = Programa.objects.get(pk=1)
        todos_os_programas = Programa.objects.all()

        self.assertEqual(len(todos_os_programas), 9)
        self.assertEqual(coisas_bizarras.titulo, "Coisas bizarras")
