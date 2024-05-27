from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from movie_list_app_class_based.models import Movie_sect_2
from movie_list_app_class_based.api.serializer import Movie2Serializer


class MovieList(APIView):
    
    def get(self, request):
        movies = Movie_sect_2.objects.all()
        serialzer = Movie2Serializer(movies,many=True)
        return Response(serialzer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        serializer = Movie2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class MovieDetailAV(APIView):
    
    def get(self, request,pk):
        try:
            movies = Movie_sect_2.objects.get(pk=pk)
            serializer = Movie2Serializer(movies)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Movie_sect_2.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request,pk):
        try:
            movies = Movie_sect_2.objects.get(pk=pk)
            serializer = Movie2Serializer(movies)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def delete(self,request,pk):
        try:
            try:
                movie = Movie_sect_2.objects.get(pk=pk)
                movie.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)