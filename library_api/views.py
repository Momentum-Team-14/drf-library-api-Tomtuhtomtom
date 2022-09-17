from sqlite3 import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.serializers import ValidationError
from .models import Book, Track, Note, CustomUser
from .serializers import BookSerializer, TrackSerializer, NoteSerializer
from .permissions import IsOwnerOrReadOnly
from django.db import IntegrityError


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = ()


class FeaturedBookList(generics.ListAPIView):
    queryset = Book.objects.filter(featured=True)
    serializer_class = BookSerializer
    permission_classes = ()


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = ()


class UserTrackList(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = ()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user.id).order_by('book')


class BookTrackListCreate(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = ()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(book=self.kwargs['book_pk']).order_by('book')

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs['book_pk'])
        serializer.save(user=self.request.user, book=book)
        try: 
            serializer.save(user=self.request.user, book=book)
        except IntegrityError as error:
            raise ValidationError({"error": error})

class BookTrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = ()


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = ()


class UserNoteList(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = ()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user.id).order_by('-created_at')


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = ()


class BookNoteListCreate(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = ()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(book=self.kwargs['book_pk'], private=False).order_by('-created_at')

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs['book_pk'])
        serializer.save(user=self.request.user, book=book)


class BookNoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = ()


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'books': reverse('book-list', request=request, format=format),
        'tracks': reverse('track-list', request=request, format=format),
        'notes': reverse('note-list', request=request, format=format),
        'featured': reverse('featured-list', request=request, format=format),
    })
