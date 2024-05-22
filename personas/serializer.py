from .models import persona
from rest_framework import serializers

class personaSerializer(serializers.ModelSerializer):
    class Meta:
        model = persona
        fields = '__all__'
        