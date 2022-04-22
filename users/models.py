from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone_number = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return self.name + ': ' + str(self.phone_number)
    
    class Meta:
        verbose_name_plural = 'UserModel'
        db_table = 'UserModel'