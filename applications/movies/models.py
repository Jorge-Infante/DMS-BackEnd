from distutils.command import upload
from pyexpat import model
from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField('Titulo', max_length=60)
    subtitle = models.CharField('Subtitulo', max_length=60)
    releaseDate = models.DateField()
    director = models.CharField('Director', max_length=60)
    cover = models.ImageField(upload_to='user',blank=True , null=True)


def __str__(self):
    return str(self.id)+'-'+self.title+self.director