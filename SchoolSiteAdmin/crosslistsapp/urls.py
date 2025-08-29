from django.urls import path
from . import views


urlpatterns = [
    path('crosslists/', view=views.Crosslists_View, name='Crosslists_View'),
    path('crosslists/<str:session>/', view=views.Crosslists_View, name='Crosslists_View'),
    path('crosslists/of/<str:class_name>/', view=views.Classify_Crosslists_View, name='Classify_Crosslists_View'),
]