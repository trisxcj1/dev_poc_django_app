# imports
from django.db import models
from django.utils import timezone
import uuid

# custom imports
from company.models import Company

# employee model
class Employee(models.Model):
    """
    write doc string
    """
    # -------------------------------- Options --------------------------------
    
    # -------------------------------- Fields --------------------------------
    # ------------ employee identity information 
    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_first_name = models.CharField(max_length=200)
    employee_last_name = models.CharField(max_length=200)
    employee_linkedin_url = models.URLField(max_length=500, null=True, blank=True)
    
    # ------------ employee company information
    employee_company_id = models.ManyToManyField(Company, blank=True)
    employee_email_address = models.EmailField(max_length=200, blank=True, null=True)
    employee_title = models.CharField(max_length=200, blank=True, null=True)
    
    # ------------ employee other information
    employee_additional_notes = models.TextField(blank=True, null=True)
    
    # ------------ employee meta information
    employee_created_at = models.DateTimeField(auto_now_add=True)
    employee_updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.employee_id, self.employee_first_name, self.employee_last_name, self.employee_company_id, self.employee_created_at}'
    
    
    
    
    
    
    # # ------------ company employee information 
    # company_number_of_fulltime_employees = models.IntegerField(null=True)
    # # company_key_employees = models.CharField(max_length=150, blank=True, null=True)
    
    # # ------------ company industry information
    # company_number_of_paying_customers = models.IntegerField(null=True)
    # company_list_of_notable_customers  =  models.TextField(blank=True, null=True)
    # company_list_of_acquisitions = models.TextField(blank=True, null=True)
    # company_list_of_technology_integrations = models.TextField(blank=True, null=True)
    # # company_list_of_investors = models.TextField(blank=True, null=True)
    
    # # ------------ company location information
    # company_hq_location_city = models.CharField(max_length=150, blank=True, null=True)
    # company_hq_location_state = models.CharField(max_length=150, blank=True, null=True)
    # company_hq_location_country = models.CharField(max_length=150, blank=True, null=True)
    
    # # ------------ company other information
    # company_additional_notes = models.TextField(blank=True, null=True)
    
    # # ------------ company meta information
    # company_created_at = models.DateTimeField(auto_now_add=True)
    # company_updated_at = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #     return f'{self.company_id, self.company_legal_name, self.created_at}'