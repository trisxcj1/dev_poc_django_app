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

from .models import Company
from .serializers import CompanySerializer

# views
# ------------------------------ api overview ------------------------------
@api_view(['GET'])
def api_overview(request):
    """
    """
    api_urls = {
        'API Overview': '/api/dev',
        'API Documentation': '/api/dev/docs',
        
        # company
        'Company Information': '/api/company',
        'Company Detail': '/api/company/<str:pk>',
        
        # employee
        'Employee Information': '/api/employee',
        'Employee Detail': '/api/employee/<str:pk>',
    }
    
    return Response(api_urls)

# ------------------------------ company viewset ------------------------------
class CompanyViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
# class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#   """
#   Retrieve, update or delete a board instance.
#   """
#   queryset = Company.objects.all()
#     serializer_class = CompanySerializer