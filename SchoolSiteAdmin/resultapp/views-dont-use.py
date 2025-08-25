from django.shortcuts import render
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

# def student_terminal_result(request, pk):
#     pass_marks = 35
#     student_data = StudentModel.objects.get(id=pk)
#     session_id = getSessionID(pk)

def student_terminal_result(request,pk, *args, **kwargs):
    pass_marks = 35
    student_data = StudentModel.objects.get(id=pk)
    session_id = getSessionID(pk)


  

    first_terminal_marks = TerminalExamMarksModel.objects.filter(
            terminal_exam='first',
            academic_session = student_data.academic_session,
            class_name = student_data.class_name,
            roll_number = student_data.roll_no,
        )


    context = {
            'student' : student_data,
            'first_terminal_marks' : first_terminal_marks,
            'session_id' : session_id,
            'pass_marks' : pass_marks,
        }
    # for marks in first_terminal_marks:

    #     first_terminal_english_lang_mark = marks.english_language
    #     first_terminal_english_lit_mark = marks.english_literature
    #     first_terminal_hindi_mark = marks.hindi
    #     first_terminal_physics_mark = marks.physics
    #     first_terminal_chemistry_mark = marks.chemistry
    #     first_terminal_biology_mark = marks.biology
    #     first_terminal_history_mark = marks.history
    #     first_terminal_geography_mark = marks.geography
    #     first_terminal_mathematics_mark = marks.mathematics
    #     first_terminal_computer_mark = marks.computer
    #     first_terminal_total_marks  = marks.total_marks
    #     first_terminal_percentage  = marks.percentage
    #     first_terminal_supw  = marks.supw
    #     first_terminal_working_days = marks.working_days
    #     first_terminal_days_present = marks.days_present
    #     first_terminal_total_students = marks.total_students
    #     first_terminal_first_rank = marks.first_rank
    #     first_terminal_my_rank = marks.my_rank



    # context.update({
    #     'first_terminal_english_lang_mark':first_terminal_english_lang_mark,
    #     'first_terminal_english_lit_mark':first_terminal_english_lit_mark,
    #     'first_terminal_hindi_mark':first_terminal_hindi_mark,
    #     'first_terminal_physics_mark':first_terminal_physics_mark,
    #     'first_terminal_chemistry_mark':first_terminal_chemistry_mark,
    #     'first_terminal_biology_mark':first_terminal_biology_mark,
    #     'first_terminal_history_mark':first_terminal_history_mark,
    #     'first_terminal_geography_mark':first_terminal_geography_mark,  
    #     'first_terminal_mathematics_mark':first_terminal_mathematics_mark,
    #     'first_terminal_computer_mark':first_terminal_computer_mark,  

    #     'first_terminal_total_marks':first_terminal_total_marks,  
    #     'first_terminal_percentage':first_terminal_percentage, 
    #     'first_terminal_supw' : first_terminal_supw,

    #     'first_terminal_working_days' : first_terminal_working_days,
    #     'first_terminal_days_present' : first_terminal_days_present,
    #     'first_terminal_total_students' : first_terminal_total_students,
    #     'first_terminal_first_rank' : first_terminal_first_rank,
    #     'first_terminal_my_rank' : first_terminal_my_rank,
    # })

    # first_terminal_marks = list(TerminalExamMarksModel.objects.filter(
    #         terminal_exam='first',
    #         academic_session = student_data.academic_session,
    #         class_name = student_data.class_name,
    #         roll_number = student_data.roll_no,
    #     ).values())
    
    # first_terminal_marks = TerminalExamMarksModel.objects.filter(terminal_exam='first')

    # print('terminal roll-number english_language')
    # for record in first_terminal_marks:
    #     print("Terminal : " , record.terminal_exam)
    #     print("Roll Number : ", record.roll_number)
    #     print("English Language : ", record.english_language)
        # print(record.terminal_exam , record.roll_number, record.english_language)
 



    # first_terminal_marks = get_object_or_404(FirstExamMarksModel, student_name=student_data.student_name) 
    # first_terminal_marks = TerminalExamMarksModel.objects.get(id=pk)

    # return render(request, 'student_marksheet.html', context)


   #     {% for marks in first_terminal_marks %}
    if student_data.class_name == 'IX' or student_data.class_name == 'X':
        #  html_file = 'class_wise_marksheet/class_x_marksheet.html'
        html_file = 'test_marksheet.html'
    elif student_data.class_name == 'VI' or student_data.class_name == 'VII' or student_data.class_name == 'VIII':
        # html_file = 'class_wise_marksheet/class_vi_to_viii_marksheet.html'
        html_file = 'test_marksheet.html'
    else:
         html_file = 'test_marksheet.html'




    return render(request,html_file, context)

# Session-ID : 2025-26/X-A/01