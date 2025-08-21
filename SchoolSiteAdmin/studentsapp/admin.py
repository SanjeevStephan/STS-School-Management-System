from django.contrib import admin

# Register your models here.

from .models import StudentModel
# from .models import Student
# from .models import FirstTerminalMarks


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Info', {
            'fields' : ('student_name','father_name','mother_name','dob','aadhar_no')
        }),
        ('School Details', {
            'fields' : ('admission_no','academic_session', 'class_name','section_name','roll_no','conveyance','whatsapp_no')
        }),
        (
            'Communication Details', {
                'classes' : ('collapse'),
                'fields' : ('address','district','state','pin_code','mobile_no')
            }
        )
    )



    list_display = ('student_name','academic_session','class_name','roll_no')


# admin.site.register(Student)
# admin.site.register(FirstTerminalMarks)
admin.site.register(StudentModel, StudentAdmin)