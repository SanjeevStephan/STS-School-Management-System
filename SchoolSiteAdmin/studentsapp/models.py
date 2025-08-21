from django.db import models

# Create your models here.
from dropdownlists.models import AcademicOptionsModel
from dropdownlists.models import ClassOptionsModel
from dropdownlists.models import StateOptionsModel
from dropdownlists.models import DistrictsOptionsModel
from dropdownlists.models import SubjectsOptionsModels
from dropdownlists.models import RollNumberOptionsModels


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

SECTION_CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)

CONVEYANCE_CHOICES = (
    ('bus', 'BUS'),
    ('self', 'SELF')
)


class StudentModel(models.Model):
    # serial_no      = models.IntegerField(primary_key=True, )
    admission_no     = models.CharField(max_length=10, blank=True)         ## SHOW    
    student_name     = models.CharField(max_length=150)                    ## SHOW
    # academic_session = models.CharField(max_length=10,  default='2025-26', blank=True, null=True) ## SHOW
    academic_session = models.ForeignKey(AcademicOptionsModel, on_delete=models.CASCADE)
    father_name      = models.CharField(max_length=150, blank=True)       
    mother_name      = models.CharField(max_length=150, blank=True)        
    class_name       = models.CharField(max_length=50, choices=CLASS_CHOICES)              ## SHOW
    # class_name       = models.ForeignKey(ClassOptionsModel, on_delete=models.CASCADE, blank=True, null=True)
    section_name     = models.CharField(max_length=2,  choices=SECTION_CHOICES, default='A') 
    # roll_no          = models.IntegerField()                               ## Must ( ... , blank=True, null=True )
    roll_no          = models.ForeignKey(RollNumberOptionsModels, on_delete=models.CASCADE)  ## SHOW  
    dob              = models.DateField()                                                                           ## SHOW
    address          = models.TextField(max_length=300, blank=True)
    # district       = models.CharField(max_length=50, choices=DISTRICT_CHOICES, null=True, blank=True)
    district         = models.ForeignKey(DistrictsOptionsModel, on_delete=models.CASCADE, null=True, blank=True)
    # state          = models.CharField(max_length=50, choices=STATE_CHOICES, null=True, blank=True)
    state            = models.ForeignKey(StateOptionsModel, on_delete=models.CASCADE, null=True, blank=True)
    pin_code         = models.IntegerField(null=True, blank=True)
    mobile_no        = models.BigIntegerField(null=True, blank=True)
    whatsapp_no      = models.BigIntegerField(null=True, blank=True)
    aadhar_no        = models.BigIntegerField(null=True, blank=True)
    conveyance       = models.CharField(max_length=5, choices=CONVEYANCE_CHOICES, blank=True, null=True)

    class Meta:
        verbose_name = 'Students Detail'


    def __str__(self):
        # return f'{self.student_name} - {self.class_name}'
        return f'{self.student_name}'