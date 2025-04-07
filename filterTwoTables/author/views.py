from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from .serializers import  AuthorSerializer, DepartmentSerializer
from .models import  Author, Department  
from .filters import AuthorFilter, DepartmentFilter   

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AuthorFilter

class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DepartmentFilter