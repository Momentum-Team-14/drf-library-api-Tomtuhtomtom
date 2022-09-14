from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CustomUser, Book, Track, Note

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'publication_date', 'genre', 'featured',)


class TrackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Track
        fields = ('id', 'user', 'book', 'status',)


class NoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Note
        fields = ('id', 'user', 'book', 'created_at', 'note', 'private', 'page',)
