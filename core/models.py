from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="E-mail")
    telefone = models.CharField(max_length=20, verbose_name="Telefone", blank=True, null=True)
    mensagem = models.TextField(verbose_name="Mensagem")
    data_envio = models.DateTimeField(auto_now_add=True, verbose_name="Data de Envio")

    class Meta:
        ordering = ['-data_envio']
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"

    def __str__(self):
        return f"{self.nome} — {self.data_envio.strftime('%d/%m/%Y')}"


class Servico(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Serviço")
    preco = models.IntegerField(verbose_name="Preço em Kz")
    descricao_curta = models.CharField(max_length=200, verbose_name="Descrição Curta")
    descricao_completa = models.TextField(verbose_name="O que inclui")
    ordem = models.IntegerField(default=0, verbose_name="Ordem de Exibição")
    ativo = models.BooleanField(default=True, verbose_name="Visível no Site")

    class Meta:
        ordering = ['ordem']
        verbose_name = "Serviço e Preço"
        verbose_name_plural = "Serviços e Preços"

    def __str__(self):
        return f"{self.nome} — {self.preco} Kz"
