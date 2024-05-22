from .models import persona
from .serializer import personaSerializer
from rest_framework import mixins,viewsets, permissions
from .pagination import resultPaginationLimit
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class personaViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    
    serializer_class = personaSerializer
    permission_classes = [permissions.AllowAny]
    queryset= persona.objects.all()
    pagination_class = resultPaginationLimit
    
    @swagger_auto_schema(operation_description="Lista todas las personas")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Crea una nueva persona")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Muestra una persona por su ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    

