from django.db import models
from datetime import datetime
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    conteudo = CKEditor5Field('Content', config_name='default')
    data_publicacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo