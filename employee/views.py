# imports
from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Employee
from .serializers import EmployeeSerializer

# views
# ------------------------------ employee viewset ------------------------------
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer