from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('marksheets/of/<str:class_name>/', view=views.Marksheets_Print_View, name='Marksheets_Print_View')
    
] 