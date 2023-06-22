from .models import project
from rest_framework import viewsets, permissions
from .serializers import projectserializer


class projectviewset(viewsets.ModelViewSet):
    queryset = project.objects.all()
    permission_class = [permissions.AllowAny]
    serializer_class = projectserializer
