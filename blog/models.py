from django.db import models
from djrichtextfield.models import RichTextField
from django.utils.timezone import now
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.name}'

class Author(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return f'{self.name}'
    
    # def get_absolute_url(self):
    #     return reverse('author', args=[str(self.name)])

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=now)
    tags = models.ManyToManyField('Tag', related_name='posts')
