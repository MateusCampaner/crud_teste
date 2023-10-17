from django.test import TestCase
from django.urls import reverse
from .models import Pessoa

class PessoaCrudTest(TestCase):
    def test_create_view(self):
        pessoa_teste = {'nome': 'Mateus'}

        response = self.client.post(reverse('Salvar'), data=pessoa_teste)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(Pessoa.objects.count(), 1)

        pessoa_criada = Pessoa.objects.first()
        self.assertEqual(pessoa_criada.nome, 'Mateus')

    def test_editar_view(self):
        pessoa_teste = Pessoa.objects.create(nome='Mateus')
        
        response = self.client.get(reverse('Editar', args=[pessoa_teste.id]))
        
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response, 'Teste')

    def test_update_view(self):
        pessoa_teste = Pessoa.objects.create(nome='Mateus')
    
        response = self.client.post(reverse('update', args=[pessoa_teste.id]), {'nome': 'Eduardo'})
        
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('app'))

        pessoa_criada = Pessoa.objects.get(id=pessoa_teste.id)
        self.assertEqual(pessoa_criada.nome, 'Eduardo')

    def test_delete_view(self):
        pessoa_teste = Pessoa.objects.create(nome='Mateus')
        
        response = self.client.post(reverse('delete', args=[pessoa_teste.id]))
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('app'))

        self.assertEqual(Pessoa.objects.count(), 0)
