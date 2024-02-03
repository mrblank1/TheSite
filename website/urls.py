from django.urls import path
from website.views import  *
app_name='website'
urlpatterns = [
    
    path('' , home,name='index'),
    path('contact' , contact_us,name='contact'),
    path('about', about, name ='about'),
    
   
]
