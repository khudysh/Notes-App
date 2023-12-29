from django.shortcuts import render
from rest_framework import generics, permissions
from .models import *
from .permisisions import IsOwnerOrReadOnly
from .serializers import *


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Фильтрация и сортировка товаров на странице
    def get_queryset(self):
        queryset = super(NoteList, self).get_queryset().order_by('id')
        # category_id = self.kwargs.get('category_id')
        sort = self.request.GET.get('sort')
        author = self.request.GET.get('author')
        if author:
            queryset = queryset.filter(owner=author)
        if sort == ('toNew'):
            queryset = queryset.order_by('created')
        if sort == ('toOld'):
            queryset = queryset.order_by('-created')
        return queryset


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
