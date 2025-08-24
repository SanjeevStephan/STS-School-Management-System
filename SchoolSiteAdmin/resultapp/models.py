from django.db import models

# Create your models here.
from studentsapp.models import StudentModel
from dropdownlists.models import ClassOptionsModel
from dropdownlists.models import RollNumberOptionsModels
# Optional: Define choices for option fields
# # Optional: Define choices for option fields
CLASS_CHOICES = (
    ('Nursery', 'Nursery'),
    ('LKG', 'LKG'),
    ('UKG', 'UKG'),
    ('I', 'Class 1'),
    ('II', 'Class 2'),
    ('III', 'Class 3'),
    ('IV', 'Class 4'),
    ('V', 'Class 5'),
    ('VI', 'Class 6'),
    ('VII', 'Class 7'),
    ('VIII', 'Class 8'),
    ('IX', 'Class 9'),
    ('X', 'Class 10'),

    # Add more as needed
)

SUPW_CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)

SESSION_CHOICES = (
    ('2024-25','2024-25'),
    ('2025-26','2025-26')
)

TERMINAL_CHOICES = (
    ('first','First Terminal'),
    ('second','Second Terminal'),
    ('third','Third Terminal'),
)

FINAL_RESULT_CHOICES = (
    ('passed','PASSED'),
    ('promoted','PROMOTED')
)


current_session = '2025-26'

# Create your models here.
class TerminalExamMarksModel(models.Model):
    # student_name = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200, blank=True, null=True)
    class_name   = models.CharField(max_length=20, choices=CLASS_CHOICES)
    academic_session = models.CharField(max_length=10, choices=SESSION_CHOICES) ## SHOW
    terminal_exam  = models.CharField(max_length=6, choices=TERMINAL_CHOICES)
    # class_name     = models.ForeignKey(ClassOptionsModel, on_delete=models.CASCADE, blank=True,null=True)
    roll_number    = models.ForeignKey(RollNumberOptionsModels, on_delete=models.CASCADE, blank=True, null=True)
    ## First Terminal Subject's Marks 
    english    = models.IntegerField(blank=True, null=True)
    english_language  = models.IntegerField(blank=True, null=True)
    english_literature = models.IntegerField(blank=True, null=True)
    hindi      = models.IntegerField(blank=True, null=True)
    sanskrit   = models.IntegerField(blank=True, null=True)
    social_studies = models.IntegerField(blank=True, null=True)
    moral_science = models.IntegerField(blank=True, null=True)    
    general_knowledge = models.IntegerField(blank=True, null=True)    


    ## Science Subjects
    physics      = models.IntegerField(blank=True, null=True) 
    chemistry    = models.IntegerField(blank=True, null=True) 
    biology      = models.IntegerField(blank=True, null=True) 
    mathematics  = models.IntegerField(blank=True, null=True) 
    computer     = models.IntegerField(blank=True, null=True)    


    ## Junior Classes Subjects
    drawing = models.IntegerField(blank=True, null=True)    
    handwriting = models.IntegerField(blank=True, null=True)    
    conversation = models.IntegerField(blank=True, null=True)    
    rhymes = models.IntegerField(blank=True, null=True)    
    environmental_studies = models.IntegerField(blank=True, null=True)    
    english_hindi_reading = models.IntegerField(blank=True, null=True)   
    ## Higher Classes Subjects 
    history = models.IntegerField(blank=True, null=True)    
    geography = models.IntegerField(blank=True, null=True)    


    total_marks = models.IntegerField(blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)
    supw = models.CharField(max_length=1, choices=SUPW_CHOICES, blank=True, null=True)

    ## Attendance_days
    working_days = models.IntegerField(blank=True, null=True)
    days_present = models.IntegerField(blank=True, null=True)
    ## students strength
    total_students = models.IntegerField(blank=True, null=True)
    ## 
    first_rank  = models.IntegerField(blank=True, null=True)
    my_rank     = models.IntegerField(blank=True, null=True)

    final_result = models.CharField(max_length=10, choices=FINAL_RESULT_CHOICES, blank=True, null=True)


    def __str__(self):
        return f'{self.student_name} '
    

    # - Class {self.class_name}