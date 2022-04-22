from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from users.views import Welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', Welcome.as_view()),
    
    # Users App Routing
    path('user/', include('users.urls')),
    
    # Plans App Routing
    path('plan/', include('plans.urls')),
    
    # Subscriptions App Routing
    path('subscription/', include('subscriptions.urls')),
    
]
