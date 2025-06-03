from django.db import models

from app.models import BaseModel


class Genre(BaseModel):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
