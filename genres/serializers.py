from rest_framework import serializers

from genres.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format='%d-%m-%Y %H:%M', read_only=True
    )
    updated_at = serializers.DateTimeField(
        format='%d-%m-%Y %H:%M', read_only=True
    )

    class Meta:
        model = Genre
        fields = ('id', 'name', 'created_at', 'updated_at')


class GenreSerializerName(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'created_at', 'updated_at')
