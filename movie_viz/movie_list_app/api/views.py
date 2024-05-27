from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from movie_list_app.models import Movie
from movie_list_app.api.serializer import MovieSerializer
from rest_framework import status

@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        try:
            movie = Movie.objects.all()
            serializer = MovieSerializer(movie,many=True)
            return Response({
                'data':serializer.data,
                
                'success' : True
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'success': False
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
            serializer = MovieSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
@api_view(['GET','PUT','DELETE'])
def movie_details(request,pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie,status=status.HTTP_200_OK)
            return Response({
                'data' : serializer.data,
                'success' : True
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message' : 'Reccord not found',
                'success' : False
            }, status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
            