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

GRADE_CHOICES = (
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
    ('FAILED','FAILED'),
    ('PASSED','PASSED'),
    ('PROMOTED','PROMOTED')
)

current_session = '2025-26'

# Create your models here.
class TerminalExamMarksModel(models.Model):
    # student_name = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    student_name     = models.CharField(max_length=200, blank=True, null=True)
    class_name       = models.CharField(max_length=20, choices=CLASS_CHOICES)
    academic_session = models.CharField(max_length=10, choices=SESSION_CHOICES) ## SHOW
    terminal_exam    = models.CharField(max_length=6, choices=TERMINAL_CHOICES)
    # class_name     = models.ForeignKey(ClassOptionsModel, on_delete=models.CASCADE, blank=True,null=True)
    roll_number      = models.ForeignKey(RollNumberOptionsModels, on_delete=models.CASCADE, blank=True, null=True)
    
    ## First Terminal Subject's Marks 
    english             = models.IntegerField(default=0)
    english_language    = models.IntegerField(default=0)
    english_literature  = models.IntegerField(default=0)
    hindi               = models.IntegerField(default=0)
    sanskrit            = models.IntegerField(default=0)
    social_studies      = models.IntegerField(default=0)
    moral_science       = models.IntegerField(default=0)    
    general_knowledge   = models.IntegerField(default=0)    

    ## Science Subjects
    science      = models.IntegerField(default=0) 
    physics      = models.IntegerField(default=0) 
    chemistry    = models.IntegerField(default=0) 
    biology      = models.IntegerField(default=0) 
    mathematics  = models.IntegerField(default=0) 
    computer     = models.IntegerField(default=0)    

    ## Junior Classes Subjects | GRADE
    drawing     = models.CharField(max_length=1, choices=GRADE_CHOICES, blank=True, null=True)
    handwriting = models.CharField(max_length=1, choices=GRADE_CHOICES, blank=True, null=True)
    reading     = models.CharField(max_length=1, choices=GRADE_CHOICES, blank=True, null=True)
    spelling    = models.IntegerField(default=0)    
    dictation   = models.IntegerField(default=0)    
    supw = models.CharField(max_length=1, choices=GRADE_CHOICES, blank=True, null=True)

    conversation = models.IntegerField(default=0)    
    rhymes = models.IntegerField(default=0)    
    environmental_studies = models.IntegerField(default=0)    

    ## Higher Classes Subjects 
    history   = models.IntegerField(default=0)    
    geography = models.IntegerField(default=0)    

    total_marks = models.IntegerField(default=0)
    percentage  = models.DecimalField(max_digits=5, decimal_places=2,blank=True, null=True)

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