from django.urls import path
from users.views import AddUser, ViewUserPlan

urlpatterns = [

    path('addUser/', AddUser.as_view()),
    
    path('viewUserPlan/', ViewUserPlan.as_view()),

]
