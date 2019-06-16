from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    #path('', views.home, name="home"),
    path('user_login/', views.user_login, name="user_login"),
    # path('student_view/', views.student_view, name='student_view'),
    path('about/', views.about, name='about'),
    # path('student_login/', views.student_login, name='student_login'),
    # path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('parents_login/', views.parents_login, name='parents_login'),
    path('student_view/', views.student_view, name='student_view'),
    # path('<int:pk>/',views.student_detail),
    # path('<int:pk>/',views.StudentAttendanceView.as_view(),name='Attendance'),
    path('Attendances/', views.StudentAttendanceView.as_view(), name='Attendances'),
    path('details/', views.student_view, name='details'),
    path('Marks/', views.StudentExamView.as_view(), name='Marks'),
    # path('Attendances/', views.student_attendance, name='Attendances'),
    path('Marks/', views.ParentExamView.as_view(), name='Marks_obt'),
]
# (?P<pk>\d+)/$
# student_view/Attendances/
