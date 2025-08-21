from django.shortcuts import render
from django.conf import settings
from .models import StudentModel


logo = f"{settings.STATIC_URL}{'img/govt-of-india-logo.png'}"
website = {
'title' : "St.Thomas School",
'link'  : '',
'logo'  : logo
}


nav_menu = [
    {
        'name' : 'LKG',
        'link' : "/student/LKG",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'UKG',
        'link' : "/student/UKG",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class I',
        'link' : "/student/I",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class II',
        'link' : "/student/II",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class III',
        'link' : "/student/III",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class IV',
        'link' : "/student/IV",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class V',
        'link' : "/student/V",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class VI',
        'link' : "/student/VI",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class VII',
        'link' : "/student/VII",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class VIII',
        'link' : "/student/VIII",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class IX',
        'link' : "/student/IX",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class X',
        'link' : "/student/X",
        'icon' : 'bi bi-person'
    }
]

govt_exams = [
    {
        'name' : 'IBPS',
        'link' : "/student/IBPS",
        'icon' : 'bi bi-bookmark-star-fill'
    },
    {
        'name' : 'JSSC',
        'link' : "/student/JSSC",
        'icon' : 'bi bi-bookmark-star-fill'
    }
    ,
    {
        'name' : 'UPSC',
        'link' : "/exams/govt/UPSC",
        'icon' : 'bi bi-bookmark-star-fill'
    }
]

context =  {
    'studentdb' : StudentModel.objects.all(),
    'nav_menu' : nav_menu,
    'govt_exams' : govt_exams,
    'alias_name' : 'all',
    'website' : website
}



# Create your views here.
def StudentView(request):
    return render(request, 'all_students.html', context)


def Filter_Students_Via_Class(request, *args, **kwargs):
    class_name = kwargs.get('class_name')
    # context.update({'class_name' : class_name})
    context.update({'alias_name' : class_name})
    # context.update({'site_title' : 'All Students Records'})
    return render(request, 'all_students.html', context)


