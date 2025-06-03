from django.contrib import admin

from actors.models import Actor


@admin.register(Actor)
class ActorModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'genre',
        'nationality',
        'birthday',
    )
    ordering = ('id',)
