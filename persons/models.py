from django.db import models


class Person(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=128)
    last_name = models.CharField(verbose_name='Last Name', max_length=128)
    email = models.EmailField(verbose_name='Email', unique=True)
    age = models.PositiveIntegerField(verbose_name='Age', null=True, blank=True)
    bio = models.TextField(verbose_name='Bio', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Created At', auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
