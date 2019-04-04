from django.contrib import admin
from .models import Teacher, Object
# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name_tea', 'address']
    search_fields = ['name_tea']
    list_filter = ['address']

class ObjectAdmin(admin.ModelAdmin):
    list_display = ['teach', 'name_obj', 'credit']
    search_fields = ['name_obj']
    list_filter = ['teach', 'name_obj']

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Object, ObjectAdmin)