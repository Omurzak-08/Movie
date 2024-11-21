from  rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from  rest_framework.filters import SearchFilter, OrderingFilter


class ProfileViwSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all
    serializer_class = CountrySerializer


class  DirectorViewSet(viewsets.ModelViewSet):
    queryset =  Director.objects.all
    serializer_class =  DirectorSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all
    serializer_class = ActorSerializer



class JanreViewSet(viewsets.ModelViewSet):
    queryset = Janre.objects.all
    serializer_class = JanreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset =Movie.objects.all
    serializer_class = MomentsSerializer


class MovieLanguagesViewSet(viewsets.ModelViewSet):
    queryset = MovieLanguages.objects.all
    serializer_class = MovieLanguagesLangSerializer


class MomentsViewSet(viewsets.ModelViewSet):
    queryset = Moments.objects.all
    serializer_class = MomentsSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class FavoriteMovieViewSet(viewsets.ModelViewSet):
        queryset = Favorite.objects.all()
        serializer_class = FavoriteMovieSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class MovieListViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ['movie_name']
    ordering_fields = ['movie_name', 'year']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MovieDetailViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]