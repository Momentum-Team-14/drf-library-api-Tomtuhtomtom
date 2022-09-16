from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library_api import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name="book-list"),
    path('books/<int:pk>/', views.BookDetail.as_view(), name="book-detail"),
    path('tracks/', views.UserTrackList.as_view(), name="track-list"),
    path('tracks/<int:pk>/', views.TrackDetail.as_view(), name="track-detail"),
    path('books/<int:book_pk>/tracks/', views.BookTrackListCreate.as_view(), name="book-track-list"),
    path('books/<int:book_pk>/tracks/<int:pk>', views.BookTrackDetail.as_view(), name="book-track-detail"),
    path('notes/', views.UserNoteList.as_view(), name="note-list"),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name="note-detail"),
    path('books/<int:book_pk>/notes/', views.BookNoteListCreate.as_view(), name="book-note-list"),
    path('books/<int:book_pk>/notes/<int:pk>', views.BookNoteDetail.as_view(), name="book-note-detail"),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
