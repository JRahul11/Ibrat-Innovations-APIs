from ast import Add
from django.urls import path
from plans.views import GetPlans, AddPlan

urlpatterns = [

    path('getPlans/', GetPlans.as_view()),
    
    path('addPlan/', AddPlan.as_view()),

] 
