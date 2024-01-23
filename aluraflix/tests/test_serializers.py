from django.test import TestCase

from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):
    def setUp(self):
        self.programa = Programa(
            titulo="Titulo do Programa 1",
            data_lancamento="2003-01-01",
            likes=10,
            dislikes=10,
            tipo="F",
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verifica_campos_serializados(self):
        """Teste que verifica os campos serializados do programa"""
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()),
            set(["titulo", "tipo", "data_lancamento", "likes"]),
        )

    def test_verifica_o_conteudo_dos_campos_serializados(self):
        """Teste que verifica o conteudo dos campos serializados do programa"""
        data = self.serializer.data
        self.assertEqual(data["titulo"], self.programa.titulo)
        self.assertEqual(
            data["data_lancamento"], self.programa.data_lancamento
        )
        self.assertEqual(data["likes"], self.programa.likes)
        self.assertEqual(data["tipo"], self.programa.tipo)
