from django.db.models import Avg
from rest_framework import serializers

from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'resume',
            'genre',
            'release_date',
            'actors',
            'created_at',
            'updated_at',
        )

    def validate_release_date(self, value):
        year_validate = 1990
        if not value:
            return value
        if value.year < year_validate:
            raise serializers.ValidationError(
                f'Data de lançamento não pode ser menor que {year_validate}'
            )
        return value

    def validate_resume(self, value):
        MAX_DIGITS = 500
        if len(value) > MAX_DIGITS:
            raise serializers.ValidationError(
                'Não pode cadastrar acima de 200 caracteres'
            )
        return value

    def validate_actors(self, value):
        if not value:
            raise serializers.ValidationError(
                'Filmes não podem ser cadastrados sem atores'
            )
        return value


class MovieListSerializer(MovieModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateTimeField(
        format='%d-%m-%Y %H:%M', read_only=True
    )
    updated_at = serializers.DateTimeField(
        format='%d-%m-%Y %H:%M', read_only=True
    )
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
