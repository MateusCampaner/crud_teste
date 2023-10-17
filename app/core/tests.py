from django.test import TestCase
from django.urls import reverse
from .models import Pessoa

class PessoaCrudTest(TestCase):
    def test_salvar_view(self):
        pessoa_teste = {'nome': 'Teste'}

        response = self.client.post(reverse('salvar'), data=pessoa_teste)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(Pessoa.objects.count(), 1)

        pessoa_criada = Pessoa.objects.first()
        self.assertEqual(pessoa_criada.nome, 'Teste')

    def test_editar_view(self):
        pessoa_teste = Pessoa.objects.create(nome='Teste')
        
        response = self.client.get(reverse('editar', args=[pessoa_teste.id]))
        
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response, 'Teste')

    def test_update_view(self):
        pessoa_teste = Pessoa.objects.create(nome='Teste')
    
        response = self.client.post(reverse('update', args=[pessoa_teste.id]), {'nome': 'NovoNome'})
        
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('app'))

        pessoa_criada = Pessoa.objects.get(id=pessoa_teste.id)
        self.assertEqual(pessoa_criada.nome, 'NovoNome')

    def test_delete_view(self):
        pessoa_teste = Pessoa.objects.create(nome='Teste')
        
        response = self.client.post(reverse('delete', args=[pessoa_teste.id]))
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('app'))

        self.assertEqual(Pessoa.objects.count(), 0)
