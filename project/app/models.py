from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime
from django import forms
# from django.core.exceptions import ValidationError


# Create your models here.


ATTENDANCE = (
    ('Present','Present'),
    ('Absent','Absent')
)
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department,related_name='course' ,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    department = models.ForeignKey(Department, related_name='subject',on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, related_name='subject',on_delete=models.CASCADE, null=True)
    subject_name = models.CharField(max_length=50,null=True)
    # subject_teacher = models.CharField(max_length=70, null=True)
    # credits = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.subject_name

    # def __str__(self):
    #     return self.subject_teacher

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    #roll_no = models.IntegerField()
    department = models.ForeignKey(Department,related_name='student', on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course,related_name='student', on_delete=models.CASCADE, null=True)
    subject_name = models.ManyToManyField(Subject, related_name='student')


    def __str__(self):
        if self.first_name and not self.last_name:
            return self.first_name
        elif self.first_name and self.last_name:
            return self.first_name + '' + self.last_name
        else:
            return 'Student'
#
# def create_profile(sender,**kwargs):
#     if kwargs['created']:
#         student = student.object.create(user=kwargs['instance'])
#
# post_save.connect(create_profile, sender=User)

class Student_Attendance(models.Model):
    student = models.ForeignKey(User,related_name='student_attendance', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    present = models.CharField(max_length=20,choices=ATTENDANCE)

    def __str__(self):
        return self.student.student.first_name + '' + self.student.student.last_name

    # def __bool__(self):
    #     return self.present

    def get_type(self):
        if self.present:
            return 'Present'
        else:
            return 'Absent'

class Exam(models.Model):
    course = models.ForeignKey(Course,related_name='exam', on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(User,related_name='exam', on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, related_name='exams',on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(null=True)
    student_marks = models.FloatField(default=0.0)
    out_off = models.IntegerField(default=100)
    # subject_teacher = models.ForeignKey(Subject, related_name='exam', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.student.student.first_name + '' + self.student.student.last_name

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, related_name='Parent', on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=50, null=True)



    def __str__(self):
        if self.first_name and not self.last_name:
            return self.first_name
        elif self.first_name and self.last_name:
            return self.first_name + '' + self.last_name
        else:
            return 'Parent'
# def create_profile(sender,**kwargs):
#     if kwargs['created']:
#         parents = parents.object.create(user=kwargs['instance'])
#
# post_save.connect(create_profile, sender=User)
