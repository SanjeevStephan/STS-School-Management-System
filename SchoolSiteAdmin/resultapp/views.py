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

# def student_terminal_result(request, pk):
#     pass_marks = 35
#     student_data = StudentModel.objects.get(id=pk)
#     session_id = getSessionID(pk)

def get_remarks(first_terminal_percentage):
    if 90 <= first_terminal_percentage <= 100:
        return 'EXCELLENT'
    elif 80 <= first_terminal_percentage < 90:
        return 'VERY GOOD'
    elif 60 <= first_terminal_percentage < 80:
        return 'GOOD'
    elif 40 <= first_terminal_percentage < 60:
        return 'FARE'
    elif 0 <= first_terminal_percentage < 40:
        return 'FAILURE'


    # if first_terminal_percentage >= 90 : 
    #     return 'EXCELLENT'   
    # elif first_terminal_percentage >= 80:
    #     return 'VERY GOOD' 
    # elif first_terminal_percentage >= 60:
    #     return 'GOOD'
    # elif first_terminal_percentage >= 40:
    #     return 'FARE'
    # else :
    #     return 'FAILURE'

def get_rank(first_terminal_my_rank):
    if first_terminal_my_rank is None or first_terminal_my_rank == "None":
        return ""
    
    try:
        rank = int(first_terminal_my_rank)
        # suffix = {1 : "st", 2 : "nd", 3 : "rd"}
        # return f"{rank}{suffix}"
        if first_terminal_my_rank == 1 : 
            return f'{first_terminal_my_rank}st'   
        elif first_terminal_my_rank == 2 : 
            return f'{first_terminal_my_rank}nd'   
        elif first_terminal_my_rank == 3 : 
            return f'{first_terminal_my_rank}rd'   
        else :
            return f'{first_terminal_my_rank}th'   
    except ValueError:
        return ""
  
    # except ValueError:
    #     return ''



def student_terminal_result(request,pk, *args, **kwargs):
    # lang_pass_marks = 
    # rest_subj_pass_marks = 
    # min_grade = 
    student_data = StudentModel.objects.get(id=pk)
    session_id = getSessionID(pk)

    first_terminal_marks = TerminalExamMarksModel.objects.filter(
            terminal_exam='first',
            academic_session = student_data.academic_session,
            class_name = student_data.class_name,
            roll_number = student_data.roll_no,
        )

    # first_terminal_english_lang_mark = 0
    # first_terminal_english_lit_mark = 0
    # first_terminal_hindi_mark = 0
    # first_terminal_physics_mark = 0
    # first_terminal_chemistry_mark = 0
    # first_terminal_biology_mark = 0
    # first_terminal_history_mark = 0
    # first_terminal_geography_mark = 0
    # first_terminal_mathematics_mark = 0
    # first_terminal_computer_mark = 0
    # first_terminal_total_marks  = 0
    # first_terminal_percentage  = 0
    # first_terminal_supw  = marks.supw
    # first_terminal_working_days = 0
    # first_terminal_days_present = 0
    # first_terminal_total_students = 0
    # first_terminal_first_rank = 0
    # first_terminal_my_rank = 0

    for marks in first_terminal_marks:

        first_terminal_english_mark = marks.english
        first_terminal_english_lang_mark = marks.english_language
        first_terminal_english_lit_mark = marks.english_literature
        first_terminal_hindi_mark = marks.hindi
        first_terminal_sanskrit_mark = marks.sanskrit
        first_terminal_social_studies_mark = marks.social_studies
        first_terminal_moral_science_mark = marks.moral_science
        first_terminal_general_knowledge_mark = marks.general_knowledge
       
        first_terminal_science_mark = marks.science
        first_terminal_physics_mark = marks.physics
        first_terminal_chemistry_mark = marks.chemistry
        first_terminal_biology_mark = marks.biology
        first_terminal_mathematics_mark = marks.mathematics
        first_terminal_computer_mark = marks.computer

        first_terminal_drawing_mark = marks.drawing
        first_terminal_handwriting_mark  = marks.handwriting
        first_terminal_reading_mark = marks.reading
        first_terminal_spelling_mark = marks.spelling
        first_terminal_dictation_mark = marks.dictation

        first_terminal_supw  = marks.supw

        first_terminal_conversation_mark = marks.conversation
        first_terminal_rhymes_mark = marks.rhymes

        first_terminal_environmental_studies = marks.environmental_studies
        first_terminal_history_mark = marks.history
        first_terminal_geography_mark = marks.geography
  
        first_terminal_total_marks  = marks.total_marks
        first_terminal_percentage  = marks.percentage

        first_terminal_working_days = marks.working_days
        first_terminal_days_present = marks.days_present
        first_terminal_total_students = marks.total_students

        first_terminal_first_rank = marks.first_rank
        first_terminal_my_rank = marks.my_rank
        # first_terminal_spelling_marks = marks.spelling
        final_result = marks.final_result

    context = {
        'student' : student_data,
        'first_terminal_marks' : first_terminal_marks,
        'session_id' : session_id,
        'lang_pass_marks' : 40,
        'min_grade' : "C",
        'rest_subj_pass_marks' : 35,
        'lkg_ukg_full_marks' : 100,
        'lkg_ukg_pass_marks' : 35,
        'first_terminal_english_mark' : first_terminal_english_mark,
        'first_terminal_english_lang_mark':first_terminal_english_lang_mark,
        'first_terminal_english_lit_mark':first_terminal_english_lit_mark,
        'first_terminal_hindi_mark':first_terminal_hindi_mark,
        'first_terminal_sanskrit_mark' : first_terminal_sanskrit_mark,
        'first_terminal_social_studies_mark' : first_terminal_social_studies_mark,
        'first_terminal_moral_science_mark' : first_terminal_moral_science_mark,
        'first_terminal_general_knowledge_mark' : first_terminal_general_knowledge_mark,
        'first_terminal_science_mark' : first_terminal_science_mark,
        'first_terminal_physics_mark':first_terminal_physics_mark,
        'first_terminal_chemistry_mark':first_terminal_chemistry_mark,
        'first_terminal_biology_mark':first_terminal_biology_mark,
        'first_terminal_mathematics_mark':first_terminal_mathematics_mark,
        'first_terminal_computer_mark':first_terminal_computer_mark,  

        'first_terminal_drawing_mark' : first_terminal_drawing_mark,
        'first_terminal_handwriting_mark' : first_terminal_handwriting_mark,
        'first_terminal_reading_mark' : first_terminal_reading_mark,
        'first_terminal_spelling_mark' : first_terminal_spelling_mark,
        'first_terminal_dictation_mark' : first_terminal_dictation_mark,
        'first_terminal_supw' : first_terminal_supw,
        'first_terminal_conversation_mark' : first_terminal_conversation_mark,
        'first_terminal_ryhmes_mark' : first_terminal_rhymes_mark,
        'first_terminal_environmental_studies' : first_terminal_environmental_studies,

        'first_terminal_history_mark':first_terminal_history_mark,
        'first_terminal_geography_mark':first_terminal_geography_mark,  

        'first_terminal_total_marks':first_terminal_total_marks,  
        'first_terminal_percentage':first_terminal_percentage, 

        'first_terminal_working_days' : first_terminal_working_days,
        'first_terminal_days_present' : first_terminal_days_present,
        'first_terminal_total_students' : first_terminal_total_students,
        'first_terminal_first_rank' : first_terminal_first_rank,
        'first_terminal_my_rank' : get_rank(first_terminal_my_rank),
        'student_remarks' : get_remarks(first_terminal_percentage),
    


        'final_result' : final_result
    }

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
    if student_data.class_name == 'LKG':
        # html_file =  'class_wise_marksheet/class_lkg_marksheet.html'
        context.update({'total_full_marks' : 600})  # DONE
        context.update({'total_pass_marks' : 220})
        html_file = 'terminal_wise_marksheet/class_lkg_marksheet.html'
    elif student_data.class_name == 'UKG':
        context.update({'total_full_marks' : 700}) ## DONE
        context.update({'total_pass_marks' : 255})
        html_file = 'terminal_wise_marksheet/class_ukg_marksheet.html'
    elif student_data.class_name == 'I' or student_data.class_name == 'II':
        # html_file =  'class_wise_marksheet/class_i_and_ii_marksheet.html'
        # html_file =  'terminal_wise_marksheet/for_first_terminal_only/class_i_and_ii_marksheet.html'
        context.update({'total_full_marks' : 1000}) # DONE
        context.update({'total_pass_marks' : 365})
        html_file = 'terminal_wise_marksheet/class_i_and_ii_marksheet.html'
    elif student_data.class_name == 'III':
        context.update({'total_full_marks' : 1100 }) # DONE
        context.update({'total_pass_marks' : 400})
        html_file = "terminal_wise_marksheet/class_iii_marksheet.html"
    elif student_data.class_name == 'IV':
        # html_file = "class_wise_marksheet/class_iv_marksheet.html"
        context.update({'total_full_marks' : 1100}) ## DONE
        context.update({'total_pass_marks' : 400})  
        html_file = 'terminal_wise_marksheet/class_iv_marksheet.html'
    elif student_data.class_name == 'V':
        # html_file =  'class_wise_marksheet/class_v_marksheet.html'
        context.update({'total_full_marks' : 1000})  ## DONE
        context.update({'total_pass_marks' : 365})   
        html_file = 'terminal_wise_marksheet/class_v_marksheet.html'
    elif student_data.class_name == 'VI' or student_data.class_name == 'VII':
        context.update({'total_full_marks' : 1300})
        context.update({'total_pass_marks' : 470})
        # html_file = 'class_wise_marksheet/class_vi_to_vii_marksheet.html'  
        html_file = 'terminal_wise_marksheet/class_vi_to_vii_marksheet.html'
    elif student_data.class_name == 'VIII':
        # html_file = 'class_wise_marksheet/class_viii_marksheet.html'
        context.update({'total_full_marks' : 1200}) # DONE
        context.update({'total_pass_marks' : 435})
        html_file = 'terminal_wise_marksheet/class_viii_marksheet.html'
    elif student_data.class_name == 'IX' or student_data.class_name == 'X':
        context.update({'total_full_marks' : 1000})
        context.update({'total_pass_marks' : 365})
        # html_file = 'modified_marksheet/class_xi_to_x_marksheet.html'
        html_file = 'terminal_wise_marksheet/class_ix_to_x_marksheet.html'

    # elif student_data.class_name == 'IV' :
    #      html_file =  'class_wise_marksheet/class_iv_marksheet.html'
    else:
         html_file = 'student_marksheet.html'

    context['class_ix_x_total_marks']   = first_terminal_english_lang_mark + first_terminal_english_lit_mark + first_terminal_hindi_mark + first_terminal_physics_mark + first_terminal_chemistry_mark + first_terminal_biology_mark + first_terminal_history_mark + first_terminal_geography_mark + first_terminal_mathematics_mark + first_terminal_computer_mark
    context['class_viii_total_marks']   = first_terminal_english_lang_mark + first_terminal_english_lit_mark + first_terminal_hindi_mark + first_terminal_physics_mark + first_terminal_chemistry_mark + first_terminal_biology_mark + first_terminal_history_mark + first_terminal_geography_mark + first_terminal_mathematics_mark + first_terminal_computer_mark + first_terminal_general_knowledge_mark + first_terminal_moral_science_mark
    context['class_vi_vii_total_marks'] = first_terminal_english_lang_mark + first_terminal_english_lit_mark + first_terminal_hindi_mark + first_terminal_sanskrit_mark + first_terminal_physics_mark + first_terminal_chemistry_mark + first_terminal_biology_mark + first_terminal_history_mark + first_terminal_geography_mark + first_terminal_mathematics_mark + first_terminal_computer_mark + first_terminal_general_knowledge_mark + first_terminal_moral_science_mark
    context['class_v_total_marks']      = first_terminal_english_lang_mark + first_terminal_english_lit_mark + first_terminal_hindi_mark + first_terminal_sanskrit_mark + first_terminal_science_mark + first_terminal_mathematics_mark + first_terminal_social_studies_mark + first_terminal_computer_mark + first_terminal_moral_science_mark + first_terminal_general_knowledge_mark
    context['class_iv_total_marks']     = first_terminal_english_lang_mark + first_terminal_english_lit_mark + first_terminal_hindi_mark + first_terminal_science_mark + first_terminal_mathematics_mark + first_terminal_social_studies_mark + first_terminal_computer_mark + first_terminal_moral_science_mark + first_terminal_general_knowledge_mark + first_terminal_conversation_mark + first_terminal_spelling_mark
    context['class_iii_total_marks']    = first_terminal_english_lang_mark + first_terminal_english_lit_mark + first_terminal_hindi_mark + first_terminal_science_mark + first_terminal_mathematics_mark + first_terminal_social_studies_mark + first_terminal_computer_mark + first_terminal_moral_science_mark + first_terminal_general_knowledge_mark + first_terminal_conversation_mark + first_terminal_spelling_mark
    context['class_i_ii_total_marks']   = first_terminal_english_lang_mark + first_terminal_english_lit_mark + first_terminal_hindi_mark + first_terminal_science_mark + first_terminal_mathematics_mark + first_terminal_computer_mark + first_terminal_moral_science_mark + first_terminal_general_knowledge_mark + first_terminal_conversation_mark + first_terminal_dictation_mark 
    context['class_ukg_total_marks']    = first_terminal_english_mark + first_terminal_hindi_mark + first_terminal_mathematics_mark + first_terminal_environmental_studies + first_terminal_conversation_mark + first_terminal_dictation_mark + first_terminal_rhymes_mark
    context['class_lkg_total_marks']    = first_terminal_english_mark + first_terminal_hindi_mark + first_terminal_mathematics_mark + first_terminal_conversation_mark + first_terminal_dictation_mark + first_terminal_rhymes_mark

    return render(request,html_file, context)

# Session-ID : 2025-26/X-A/01
