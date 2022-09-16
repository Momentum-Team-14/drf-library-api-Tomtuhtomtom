from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CustomUser, Book, Track, Note

class BookSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Book
        fields = ('url', 'id', 'title', 'author', 'publication_date', 'genre', 'featured',)


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    book = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Track
        fields = ('url', 'id', 'user', 'book', 'status',)


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    book = serializers.SlugRelatedField(slug_field="title", read_only=True)
    
    class Meta:
        model = Note
        fields = ('url', 'id', 'user', 'book', 'created_at', 'note', 'private', 'page',)
