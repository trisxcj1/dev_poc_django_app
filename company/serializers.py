# imports
from rest_framework import serializers
from .models import Company

# serializer
class CompanySerializer(serializers.ModelSerializer):
    """
    """
    
    class Meta:
        model = Company
        fields = '__all__'