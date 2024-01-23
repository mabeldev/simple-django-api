from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("programas-list")
        self.user = User.objects.create_user(
            username="testuser",
            password="1234",
        )

    def test_autenticacao_de_user_com_credenciais_corretas(self):
        """Teste que verifica a autenticacao de um user com credenciais corretas"""
        user = authenticate(username="testuser", password="1234")
        self.assertTrue(user is not None and user.is_authenticated)

    def test_requesicao_get_sem_autenticacao(self):
        """Teste que verifica a requisicao GET sem autenticacao"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_requesicao_get_com_autenticacao(self):
        """Teste que verifica a requisicao GET com autenticacao"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_autenticacao_de_user_com_credenciais_incorretas(self):
        """Teste que verifica a autenticacao de um user com credenciais incorretas"""
        user = authenticate(username="testuser", password="0000")
        self.assertTrue(user is None)
