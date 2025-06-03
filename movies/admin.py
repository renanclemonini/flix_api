from django.contrib import admin

from movies.models import Movie


@admin.register(Movie)
class MovieModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_actors', 'genre', 'release_date', 'resume')
    ordering = ('title',)

    def get_actors(self, obj):
        return ', '.join([actor.name for actor in obj.actors.all()])

    get_actors.short_description = 'Actors'
