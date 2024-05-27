from rest_framework import serializers
from movie_list_app_class_based.models import Movie_sect_2

class Movie2Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    
    def create(self, validated_data):
        return Movie_sect_2.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        #Compare with old data and validate it
        instance.name = validated_data.get('name', validated_data.name)
        instance.description = validated_data.get('description', validated_data.description)
        instance.active = validated_data.get('active', instance.active)
        #When validated save that object in database
        instance.save()
        #return the instance itself
        return instance
        
        