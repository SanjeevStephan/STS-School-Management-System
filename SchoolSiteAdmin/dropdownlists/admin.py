from django.contrib import admin
from .models import ClassOptionsModel
from .models import StateOptionsModel
from .models import DistrictsOptionsModel
from .models import SubjectsOptionsModels
from .models import RollNumberOptionsModels

# Register your models here.
admin.site.register(ClassOptionsModel)
admin.site.register(DistrictsOptionsModel)
admin.site.register(StateOptionsModel)
admin.site.register(SubjectsOptionsModels)
admin.site.register(RollNumberOptionsModels)
