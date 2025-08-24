from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('result/<pk>', view=views.result_app_view, name='result_app_view'),
    path('result/<str:session>/<str:class_section>/<int:roll_no>/sno/<pk>', view=views.student_terminal_result, name='student_terminal_result')

    
] 