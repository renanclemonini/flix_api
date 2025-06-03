from django.db.models import Avg, Count
from rest_framework import generics, response, status, views
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalDefaultPermission
from movies.models import Movie
from movies.serializers import (
    MovieListSerializer,
    MovieModelSerializer,
    MovieStatsSerializer,
)
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListSerializer
        return MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(
            count=Count('id')
        )
        total_reviews = Review.objects.all()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))[
            'avg_stars'
        ]

        response_data = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews.count(),
            'average_stars': round(average_stars, 1),
        }

        serializer = MovieStatsSerializer(data=response_data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.validated_data, status=status.HTTP_200_OK
        )
