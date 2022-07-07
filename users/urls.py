from urllib.parse import urlparse
from django.urls import path
from . import views
app_name='users'
urlpatterns = [
    path('add_user',views.register_api,name='add_user'),
    path('login',views.login_api,name='login'),
    
]