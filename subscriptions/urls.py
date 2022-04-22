from django.urls import path
from subscriptions.views import RechargePlan

urlpatterns = [

    path('rechargePlan/', RechargePlan.as_view()),
] 
