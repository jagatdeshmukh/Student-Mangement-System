from django.shortcuts import render
from django.shortcuts import get_object_or_404
# from django.http import HttpRequest, JsonResponse, HttpResponse
from datetime import datetime
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
from .models import Department, Course, Student, Subject, Exam, Student_Attendance #, Parent
from project import settings
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.forms import UserCreationForm
# from django.forms import inlineformset_factory
# from django.forms import modelformset_factory
from django import forms
# from django.template.defaulttags import register
# Create your views here.
from .models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from app import models

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def student_view(request,pk):
    return render(request, "app/student_view.html")

def user_login(request):
    return render(request, "app/user_login.html")

def parents_login(request):
        return render(request, "app/parents_login.html")

def home(request):
    return render(request, "app/home.html")

def about(request):
    return render(request, "app/about.html")

# def login(request):
#     return render(request,'app/login.html')

def student_view(request):
    return render(request,'app/student_view.html')

#
# class StudentDetailView(DetailView):
#     context_object_name = 'student_details'
#     model = Student
#     template_name = 'student_view.html'


def student_detail(request, pk):
    student = Student.objects.get(student_pk=pk)

    if request.user.is_authenticated:
        return render(
            request, 'student_view.html', {'student': student})
    else:
        return redirect('login')

class StudentAttendanceView(LoginRequiredMixin,ListView):
    model = Student_Attendance
    template_name = 'app/Attendances.html'
    paginate_by = 10
    context_object_name = 'Attendances'
    def get_queryset(self):
        queryset = super(StudentAttendanceView, self).get_queryset()
        queryset = queryset.filter(student_id=self.request.user)
        return queryset

class StudentExamView(LoginRequiredMixin,ListView):
    model = Exam
    template_name = 'app/Marks.html'
    paginate_by = 10
    context_object_name = 'Marks'
    def get_queryset(self):
        queryset = super(StudentExamView, self).get_queryset()
        queryset = queryset.filter(student_id=self.request.user)
        return queryset

#  N Wok
# def parent_detail(request, pk):
#     parent = Parent.objects.get(parent_pk=pk)
#
#     if request.user.is_authenticated:
#         return render(
#             request, 'student_view.html', {'parent': parent})
#     else:
#         return redirect('login')

# class ParentExamView(LoginRequiredMixin,ListView):
#     model = Exam
#     template_name = 'app/Marks.html'
#     paginate_by = 10
#     context_object_name = 'Marks_obt'
#     def get_queryset(self):
#         queryset = super(ParentExamView, self).get_queryset()
#         queryset = queryset.filter(student_pk=self.request.user)
#         return queryset

# class ParentExamView(LoginRequiredMixin,ListView):
#     model = Exam
#     template_name = 'app/Marks.html'
#     paginate_by = 10
#     context_object_name = 'Marks_obt'
#     def get_queryset(self):  # no pk parameter
#         student_attendance = get_object_or_404(student, pk=self.kwargs['pk'])
#         return self.model.objects.filter(
#             User=self.request.user,
#             student_attendance=student_attendance.id
#         )
