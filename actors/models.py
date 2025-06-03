from django.db import models

from app.models import BaseModel

NATIONALITY_CHOICES = (('USA', 'Estados Unidos'), ('BRAZIL', 'Brasil'))

GENRE_ACTOR = (('Male', 'Masculino'), ('Female', 'Feminino'))


class Actor(BaseModel):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    genre = models.CharField(choices=GENRE_ACTOR, default='Male')
    nationality = models.CharField(
        max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True
    )

    def __str__(self):
        return self.name
