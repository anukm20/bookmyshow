from django.urls import path 
from . import views
urlpatterns = [
    
    path('',views.Home,name='home'),
    path('update/<int:id>',views.Update,name='update'),
]
