from django.db import models

# Create your models here.
class ClassOptionsModel(models.Model):
    class_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Class List"
        verbose_name_plural = "Class Lists"

    def __str__(self):
        return self.class_name

class StateOptionsModel(models.Model):
    state_names = models.CharField(max_length=50)

    class Meta:
        verbose_name = "State List"
        verbose_name_plural = "State Lists"

    def __str__(self):
        return self.state_names

class DistrictsOptionsModel(models.Model):
    district_names = models.CharField(max_length=60)

    class Meta:
        verbose_name = "District List"
        verbose_name_plural = "District Lists"
    def __str__(self):
        return self.district_names

class SubjectsOptionsModels(models.Model):
    subject_name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Subjects"
        verbose_name_plural = "Subjects Lists"

    def __str__(self):
        return self.subject_name

class RollNumberOptionsModels(models.Model):
    roll_number = models.CharField(max_length=5)

    class Meta:
        verbose_name = "Roll Number"

    def __str__(self):
        return self.roll_number