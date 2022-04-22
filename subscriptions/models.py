from django.db import models
from users.models import UserModel
from plans.models import PlanModel

class SubscriptionModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    plan = models.ForeignKey(PlanModel, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.name + ' ' + self.plan.name   
    
    class Meta:
        verbose_name_plural = 'Subscription'
        db_table = 'Subscription'
