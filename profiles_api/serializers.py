from rest_framework import serializers
from profiles_api.models import  UserProfile

class HelloSerializer(serializers.Serializer):
    """serializa un campo para probar nuestra APIViews"""
    name = serializers.CharField(max_length=10)

class UserSerializer(serializers.ModelSerializer):
    """serializa un campo para probar nuestra APIViews"""
    class Meta:
        model = UserProfile
        fields = '__all__'
