from django.db import models

class PlanModel(models.Model):
    
    CATEGORY_CHOICES = (
        ('Value Plans', 'Value Plans'),
        ('Popular Plans', 'Popular Plans'),
        ('Annual Plans', 'Annual Plans')
    )
    
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True)
    price = models.PositiveIntegerField(null=True)
    validity_in_days = models.PositiveIntegerField(null=True)
    voice = models.CharField(max_length=100, null=True)
    data_per_day = models.PositiveIntegerField(null=True)
    sms_per_day = models.PositiveIntegerField(null=True)
    add_ons = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.name  
    
    class Meta:
        verbose_name_plural = 'Plan'
        db_table = 'Plan'
    
