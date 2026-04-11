from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    competencias = models.TextField()
    ects = models.IntegerField()

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=20)
    ects = models.IntegerField()
    imagem = models.ImageField(upload_to='cadeiras/', null=True, blank=True)
    link = models.URLField(max_length=300, null=True, blank=True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='unidades_curriculares')
    docentes = models.ManyToManyField(Docente, related_name='unidades_curriculares')

    def __str__(self):
        return self.nome