# imports
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CompanyViewSet

# URL configuration
router = DefaultRouter()
router.register('company', CompanyViewSet, basename='company')
urlpatterns = [
    # path('hello/', views.say_hello)
    # ...
]
urlpatterns += router.urls