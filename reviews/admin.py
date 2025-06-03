from django.contrib import admin

from reviews.models import Review


@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ('movie', 'stars', 'comment')
    ordering = ('-stars',)
