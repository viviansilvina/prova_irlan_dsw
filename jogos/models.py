from django.db import models
from .choices import tipo_modalidade

# Create your models here.
class Modalidade(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(max_length=10, choices=tipo_modalidade)
    max_atletas = models.PositiveIntegerField()

    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "Modalidades"

    def __str__(self):
        return self.nome


class Equipe(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    curso = models.CharField(max_length=50)
    cor = models.CharField(max_length=7)
    criada_em = models.DateTimeField(auto_now=True)

    class Meta:
            ordering = ["nome"]
            verbose_name_plural = "Equipes"


    def __str__(self):
        return self.nome


class Tecnico(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=50)
    equipe = models.OneToOneField(Equipe, on_delete=models.CASCADE, related_name="equipes", related_query_name="equipe")

    class Meta:
            ordering = ["nome"]
            verbose_name_plural = "Tecnicos"

    def __str__(self):
        return self.nome

class Atleta(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50, unique=True)
    data_nascimento = models.DateField()
    equipe = models.ForeignKey(Equipe, on_delete=models.PROTECT, related_name='Equipes', related_query_name="Equipe")
    modalidade = models.ManyToManyField(Modalidade, related_name="modalidades", related_query_name="modalidade")


    class Meta:
            ordering = ["nome"]
            verbose_name_plural = "Atletas"

    def __str__(self):
        return f"{self.nome}, {self.matricula}"