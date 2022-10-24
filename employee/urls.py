# imports
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import EmployeeViewSet

# URL configuration
router = DefaultRouter()
router.register('employee', EmployeeViewSet, basename='employee')
urlpatterns = [
    # ...
]
urlpatterns += router.urls