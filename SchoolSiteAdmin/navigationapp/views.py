from django.shortcuts import render
from django.conf import settings

logo = f"{settings.STATIC_URL}{'img/govt-of-india-logo.png'}"
website = {
'title' : "All Govt. Exams",
'link'  : '',
'logo'  : logo
}


nav_menu = [
    {
        'name' : 'Sanjeev Stephan Murmu',
        'link' : "/applicant/sanju",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Sanjiv Marandi',
        'link' : "/applicant/santosh",
        'icon' : 'bi bi-person'
    }
]

govt_exams = [
    {
        'name' : 'IBPS',
        'link' : "/exams/govt/IBPS",
        'icon' : 'bi bi-bookmark-star-fill'
    },
    {
        'name' : 'JSSC',
        'link' : "/exams/govt/JSSC",
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
    # 'examsdata' : examsdata.objects.all(),
    'nav_menu' : nav_menu,
    'govt_exams' : govt_exams,
    'alias_name' : 'all',
    'website' : website
}

# Create your views here.
def MainNativationView(request):
    context['exam_institution'] = ''
    context['alias_name'] = 'all'
    return render(request, 'allexams.html', context)