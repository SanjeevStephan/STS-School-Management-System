from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.StudentView, name='StudentView'),
    path('student/<str:class_name>/', view=views.Filter_Students_Via_Class, name='Filter_Students_Via_Class'),
    path('session/<str:session>/', view=views.Filter_Students_Via_Session, name='Filter_Students_Via_Class')
]