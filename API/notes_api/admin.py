from django.contrib import admin
from .models import *


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'text', 'created')
    search_fields = ['title', 'text']

    list_filter = ['created']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    search_fields = ['title']

    list_filter = ['title']
