from django.db import models
from django.utils import timezone

# Create your models here.

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ('title',)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    Publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline


    class Meta:
        ordering = ('headline',)
