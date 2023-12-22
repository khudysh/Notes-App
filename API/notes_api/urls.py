from django.urls import re_path, path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('notes/', NoteList.as_view()),
    path('notes/<int:pk>/', NoteDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)