# imports
from django.db import models
from django.utils import timezone

# company model
class Company(models.Model):
    """
    write doc string
    """
    # -------------------------------- Options --------------------------------
    corporation_type_options = (
        ('Brand', 'Brand'),
        ('Retailer', 'Retailer'),
        ('Other', 'Other')
    ) 
    
    # -------------------------------- Fields --------------------------------
    # ------------ company identity information 
    compnay_id = models.UUIDField(primary_key=True, editable=False)
    company_legal_name = models.CharField(max_length=200)
    company_website_url = models.URLField(max_length=500, null=True, blank=True)
    company_corporation_type = models.CharField(max_length=200, choices=corporation_type_options, blank=True, null=True)
    company_date_of_incorporation = models.DateField(blank=True, null=True)
    
    # ------------ company employee information 
    company_number_of_fulltime_employees = models.IntegerField(null=True)
    # company_key_employees = models.CharField(max_length=150, blank=True, null=True)
    
    # ------------ company industry information
    company_number_of_paying_customers = models.IntegerField(null=True)
    company_list_of_notable_customers  =  models.TextField(blank=True, null=True)
    company_list_of_acquisitions = models.TextField(blank=True, null=True)
    company_list_of_technology_integrations = models.TextField(blank=True, null=True)
    # company_list_of_investors = models.TextField(blank=True, null=True)
    
    # ------------ company location information
    company_hq_location_city = models.CharField(max_length=150, blank=True, null=True)
    company_hq_location_state = models.CharField(max_length=150, blank=True, null=True)
    company_hq_location_country = models.CharField(max_length=150, blank=True, null=True)
    
    # ------------ company other information
    company_additional_notes = models.TextField(blank=True, null=True)
    
    # ------------ company meta information
    company_created_at = models.DateTimeField(auto_now_add=True)
    company_updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.company_id, self.company_legal_name, self.created_at}'