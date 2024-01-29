from django.db import models

class Base(models.Model):
    visible = models.BooleanField(default=True)
    exist = models.BooleanField(default=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True) 
    
# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length=255)
    # folder = models.ForeignKey(self, on_delete=models.SET_NULL, null=True, blank=True)
    # boxCase = models.ForeignKey'BoxCase, on_delete=models.SET_NULL, null=True, blank=True)
    # shelf = models.ForeignKey(Shelf, on_delete=models.SET_NULL, null=True, blank=True)
    # warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    path = models.CharField(max_length=255)
    base_model = models.OneToOneField(Base, on_delete=models.SET_NULL, null=True, blank=True)
    
CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    ]
    
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    identification_code = models.CharField(max_length=255)
    classification_id = models.IntegerField()
    retention_period = models.DateField()
    usage_policy_start_date = models.DateField()
    usage_policy_end_date = models.DateField()
    physical_condition = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    annotation = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255)
    approval =  models.CharField(max_length=20, choices=CHOICES, default='option1')
    base_model = models.OneToOneField(Base, on_delete=models.SET_NULL, null=True, blank=True)
    
    

class watchlist(models.Model):
    # document_id = models.OneToOneField(Base, on_delete=models.SET_NULL, null=True, blank=True)
    Folder_id = models.OneToOneField(Folder, on_delete=models.SET_NULL, null=True, blank=True)
    # user_id = models.OneToOneField(user, on_delete=models.SET_NULL, null=True, blank=True)

