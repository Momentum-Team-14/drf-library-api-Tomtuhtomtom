from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=100, help_text='Enter a book title')
    author = models.CharField(max_length=100, help_text='Enter the Author')
    publication_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=100, help_text='Enter the Genre')
    featured = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['title', 'author'], name='unique_title_author')
        ]

    def __str__(self):
        return self.title


class Track(models.Model):
    WANT = 'Want to read'
    READING = 'Reading'
    READ = 'Read'
    STATUS_CHOICES = [
        (WANT, 'Want to read'),
        (READING, 'Reading'),
        (READ, 'Read'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tracks')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='tracks')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=WANT)

    class Meta:
        constraints = [
            UniqueConstraint(fields=["user", "book"], name="unique_user")
        ]

    def __str__(self):
        return f'{self.status} {self.book}'


class Note(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notes')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField(max_length=200, blank=True, null=True, help_text='Write your notes here')
    private = models.BooleanField(default=True)
    page = models.PositiveIntegerField(blank=True, null=True)


    def __str__(self):
        return self.note
