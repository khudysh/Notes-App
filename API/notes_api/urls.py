from django.urls import re_path, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

from .views import *

urlpatterns = [
    path('notes/', NoteList.as_view()),
    path('notes/<int:pk>/', NoteDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]

urlpatterns = format_suffix_patterns(urlpatterns)