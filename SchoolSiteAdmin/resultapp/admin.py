from django.contrib import admin

from .models import TerminalExamMarksModel
# Register your models here.

class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ('get_student_name','academic_session', 'terminal_exam', 'class_name','roll_number')
    list_filter = ['academic_session','terminal_exam','class_name']

    def get_student_name(self, obj):
        return obj.student_name
    get_student_name.short_description = 'Student Name'


admin.site.register(TerminalExamMarksModel, SubjectModelAdmin)

