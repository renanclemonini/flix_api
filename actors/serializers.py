from rest_framework import serializers

from actors.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(format='%d-%m-%Y', required=False)
    created_at = serializers.DateTimeField(
        format='%d-%m-%Y %H:%M', read_only=True
    )
    updated_at = serializers.DateTimeField(
        format='%d-%m-%Y %H:%M', read_only=True
    )

    class Meta:
        model = Actor
        fields = [
            'id',
            'name',
            'birthday',
            'genre',
            'nationality',
            'created_at',
            'updated_at',
        ]
