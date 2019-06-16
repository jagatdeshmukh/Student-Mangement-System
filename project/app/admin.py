from django.contrib import admin
from .models import Department,Course,Student,Subject,Exam,Student_Attendance,Parent
# from . import views
# Register your models here.

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Student_Attendance)
admin.site.register(Exam)
admin.site.register(Parent)
