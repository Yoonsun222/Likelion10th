from rest_framework import serializers
from .models import Board2

class BoardSerializer(serializers.ModelSerializer):
    class Meta :
        model = Board2    
        fields = ['title','content']