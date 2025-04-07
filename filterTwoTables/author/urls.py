from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet,  DepartmentViewSet 

router = DefaultRouter() 
router.register(r'authors', AuthorViewSet)
router.register(r'department', DepartmentViewSet, basename='department')

urlpatterns = [
    path('', include(router.urls)), 
]