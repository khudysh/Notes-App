from django.contrib.auth.models import User
from rest_framework import  serializers
from .models import *


class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.ReadOnlyField(source='category.title')

    class Meta:
        model = Note
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'notes']