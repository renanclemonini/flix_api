from django.db import models

from actors.models import Actor
from app.models import BaseModel
from genres.models import Genre


class Movie(BaseModel):
    title = models.CharField(max_length=500, unique=True)
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, related_name='movies'
    )
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(
        Actor,
        related_name='movies',
    )
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
