from django.urls import path
from movie_list_app_class_based.api.views import MovieList, MovieDetailAV


urlpatterns = [
    path('list/', MovieList.as_view(), name='movie-details'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='Movie Details ')
]
