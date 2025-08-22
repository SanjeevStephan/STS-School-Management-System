from django.shortcuts import render, get_object_or_404
from studentsapp.models import StudentModel
from resultapp.models import TerminalExamMarksModel


def getSessionID(pk):
    student_data = StudentModel.objects.get(id=pk)

    ## Generate Session ID : 
    slash = '/'
    dash = '-'
    academic_session = student_data.academic_session
    class_name = student_data.class_name
    section_name = student_data.section_name
    roll_no = student_data.roll_no

    return str(academic_session) + slash + class_name + dash + section_name + slash + str(roll_no)


# Create your views here.
def result_app_view(request, pk):
    student_data = StudentModel.objects.get(id=pk)
    context = {
        'student' : student_data
    }
    return render(request, 'marksheet.html', context)


def student_first_terminal_result(request, pk):
    pass_marks = 35
    student_data = StudentModel.objects.get(id=pk)
    session_id = getSessionID(pk)


    # first_terminal_marks = get_object_or_404(FirstExamMarksModel, student_name=student_data.student_name) 
    first_terminal_marks = FirstExamMarksModel.objects.get(id=pk)
    context = {
        'student' : student_data,
        'first_terminal_marks' : first_terminal_marks,
        'session_id' : session_id,
        'pass_marks' : pass_marks
    }
    return render(request, 'student_marksheet.html', context)

# Session-ID : 2025-26/X-A/01