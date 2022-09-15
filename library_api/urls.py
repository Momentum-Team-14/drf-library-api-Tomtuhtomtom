from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library_api import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name="book-list"),
    path('books/<int:pk>/', views.BookDetail.as_view(), name="book-detail"),
    path('books/<int:book_pk>/tracks/', views.TrackListCreate.as_view(), name="track-create"),
    path('tracks/', views.TrackList.as_view(), name="track-list"),
    path('tracks/<int:pk>/', views.TrackDetail.as_view(), name="track-detail"),
    path('notes/', views.NoteList.as_view(), name="note-list"),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name="note-detail"),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
