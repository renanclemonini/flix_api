from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from app.models import BaseModel
from movies.models import Movie


class Review(BaseModel):
    movie = models.ForeignKey(
        Movie, on_delete=models.PROTECT, related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação Minima: 0'),
            MaxValueValidator(5, 'Avaliação Máxima: 0'),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.movie}: {self.stars}'
