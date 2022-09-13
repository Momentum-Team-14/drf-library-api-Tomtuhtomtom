from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book, Track, Note

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email", "username",]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
admin.site.register(Track)
admin.site.register(Note)
