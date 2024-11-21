from .models import *
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']




class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']

class JanreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Janre
        fields = '__all__'


class MovieLanguagesLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = '__all__'

class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'



class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'description', 'movie_trailer', 'movie_image']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class MovieDetailSerializer(serializers.ModelSerializer):
 class Meta:
        model = Movie
        fields = ['movie_name','country','director','actor','genres','types','description',
                  'movie_time',  'movie_trailer', 'movie_image','status_movie','year']

 def get_average_rating(self, obj):
        return obj.get_average_rating()