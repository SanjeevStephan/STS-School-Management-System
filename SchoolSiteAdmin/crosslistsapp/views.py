from django.shortcuts import render
from django.conf import settings
from studentsapp.models import StudentModel
from resultapp.models import TerminalExamMarksModel

logo = f"{settings.STATIC_URL}{'img/school-logo.png'}"
website = {
'title' : "St.Thomas School",
'sitetitle' : "Student's Crosslists",
'link'  : '/',
'logo'  : logo
}

nav_menu = [
    {
        'name' : 'Nursery',
        'link' : "/crosslists/of/Nursery",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'LKG',
        'link' : "/crosslists/of/LKG",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'UKG',
        'link' : "/crosslists/of/UKG",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class I',
        'link' : "/crosslists/of/I",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class II',
        'link' : "/crosslists/of/II",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class III',
        'link' : "/crosslists/of/III",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class IV',
        'link' : "/crosslists/of/IV",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class V',
        'link' : "/crosslists/of/V",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class VI',
        'link' : "/crosslists/of/VI",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class VII',
        'link' : "/crosslists/of/VII",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class VIII',
        'link' : "/crosslists/of/VIII",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class IX',
        'link' : "/crosslists/of/IX",
        'icon' : 'bi bi-person'
    },
    {
        'name' : 'Class X',
        'link' : "/crosslists/of/X",
        'icon' : 'bi bi-person'
    }
]





def getTotalMarks():
    # student_data = StudentModel.objects.get(id=pk)
    # first_terminal_marks = TerminalExamMarksModel.objects.filter(
    #         terminal_exam='first',
    #         academic_session = student_data.academic_session,
    #         class_name = student_data.class_name,
    #         roll_number = student_data.roll_no,
    #     )

    terminalexam = TerminalExamMarksModel.objects.all()
    for marks in terminalexam:
        totalmarks = (
            marks.english_language + marks.english_literature + marks.hindi + marks.physics + marks.chemistry + marks.biology + 
            marks.history + marks.geography + marks.mathematics + marks.computer
    
        )
    return totalmarks


def getSessionID(pk):
    student_data = StudentModel.objects.get(id=pk)
    ## Generate Session ID : 
    slash = '/'
    dash = '-'
    # academic_session = student_data.academic_session
    academic_session = '2025-26'
    class_name = class_name
    section_name = student_data.section_name
    roll_no = student_data.roll_no

    return  academic_session + slash + class_name + dash + section_name + slash + str(roll_no)

context =  {
    'studentdb' : StudentModel.objects.all(),
    'terminalexam' : TerminalExamMarksModel.objects.all(),
    'nav_menu' : nav_menu,
    'alias_name' : 'all',
    'website' : website,
    'current_session' : '2025-25',
    'stud_total_marks' : getTotalMarks()
}


# Create your views here.
def Crosslists_View(request, *args, **kwargs):
    session = kwargs.get('session')
    context.update({'session' : session})
    return render(request, 'crosslists_of_all_students.html', context)

# Create your views here.
def Classify_Crosslists_View(request, *args, **kwargs):
    # session_id = getSessionID(pk)
    class_name = kwargs.get('class_name')
    # context.update({'class_name' : class_name})
    context.update({'alias_name' : class_name})

# class_xi_to_x_crosslists.html
#     {% for marks in first_terminal_marks %}
    if class_name == 'LKG':
        website['sitetitle'] = "Crosslist for LKG"
        html_file = 'classwise_crosslists/class_lkg_crosslists.html'
    elif class_name == 'UKG':
        website['sitetitle'] = "Crosslist for UKG"
        html_file = 'classwise_crosslists/class_ukg_crosslists.html'
    elif class_name == 'I' or class_name == 'II':
        website['sitetitle'] = "Crosslist for I | II"
        html_file = 'classwise_crosslists/class_i_ii_crosslists.html'
    elif class_name == 'III':
        website['sitetitle'] = "Crosslist for III"
        html_file = 'classwise_crosslists/class_iii_crosslists.html'
    elif class_name == 'IV':
        website['sitetitle'] = "Crosslist for IV"
        html_file = 'classwise_crosslists/class_iv_crosslists.html'
    elif class_name == 'V':
        website['sitetitle'] = "Crosslist for V"
        html_file = 'classwise_crosslists/class_v_crosslists.html'
    elif class_name == 'VI' or class_name == 'VII':
        website['sitetitle'] = "Crosslist for VI | VII"
        html_file = 'classwise_crosslists/class_vi_vii_crosslists.html'
    elif class_name == 'VIII':
        website['sitetitle'] = "Crosslist for VIII"
        html_file = 'classwise_crosslists/class_viii_crosslists.html'
    elif class_name == 'IX' or class_name == 'X':
        website['sitetitle'] = "Crosslist for IX | X"
        html_file = 'classwise_crosslists/class_xi_to_x_crosslists.html'
    else:
        html_file = 'crosslists_of_all_students.html'



    return render(request,html_file, context)
