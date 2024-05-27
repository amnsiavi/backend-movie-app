from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from movie_list_app.models import Movie
from movie_list_app.api.serializer import MovieSerializer


@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        try:
            movie = Movie.objects.all()
            serializer = MovieSerializer(movie,many=True)
            return Response({
                'data':serializer.data,
                'status':'200 ok',
                'success' : True
            })
        except:
            return Response({
                'error':'500 internal server error',
                'success': True
            })
    else:
            serializer = MovieSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)    
@api_view(['GET','PUT','DELETE'])
def movie_details(request,pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie)
            return Response({
                'data' : serializer.data,
                'code' : 'status 200 ok',
                'success' : True
            })
        except:
            return Response({
                'code' : '404 page not found',
                'message' : 'Reccord not found',
                'success' : False
            })
    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response({
            'code' : 'status 200 ok',
            'success' : True,
            'message':'reccord deleted sucessfully'
        })
        
            